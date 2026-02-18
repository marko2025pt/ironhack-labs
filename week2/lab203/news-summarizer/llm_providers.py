"""LLM provider integration with fallback support."""
# This file manages all interactions with OpenAI and Cohere.
# It also handles cost tracking, rate limiting, and fallback logic.

import time
import tiktoken
from openai import OpenAI
import cohere
from config import Config


# Simplified pricing (per million tokens – approximate)
# These values are used to estimate cost of each request.
PRICING = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "command-a-03-2025": {"input": 1.00, "output": 2.00},  # Approximate Cohere pricing
}


class CostTracker:
    """Track API costs."""

    def __init__(self):
        # Total accumulated cost across all API calls
        self.total_cost = 0.0

        # Store detailed information about each request
        self.requests = []

    def track_request(self, provider, model, input_tokens, output_tokens):
        """
        Calculate and store the cost of a single request.
        """

        # Get pricing for the model (fallback to default if not found)
        pricing = PRICING.get(model, {"input": 1.0, "output": 2.0})

        # Convert token count into USD cost
        input_cost = (input_tokens / 1_000_000) * pricing["input"]
        output_cost = (output_tokens / 1_000_000) * pricing["output"]
        cost = input_cost + output_cost

        # Add to total cost
        self.total_cost += cost

        # Save request details for later reporting
        self.requests.append({
            "provider": provider,
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost,
        })

        return cost

    def get_summary(self):
        """
        Return aggregated cost statistics.
        """
        total_input = sum(r["input_tokens"] for r in self.requests)
        total_output = sum(r["output_tokens"] for r in self.requests)

        return {
            "total_requests": len(self.requests),
            "total_cost": self.total_cost,
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "average_cost": self.total_cost / max(len(self.requests), 1),
        }

    def check_budget(self, daily_budget):
        """
        Stop execution if daily budget is exceeded.
        Warn if 90% of budget is used.
        """
        if self.total_cost >= daily_budget:
            raise Exception(f"Daily budget of ${daily_budget:.2f} exceeded!")

        percent_used = (self.total_cost / daily_budget) * 100
        if percent_used >= 90:
            print(f"⚠️ Warning: {percent_used:.1f}% of daily budget used")


def count_tokens(text, model="gpt-4o-mini"):
    """
    Estimate how many tokens a text contains.

    We try using tiktoken for accurate counting.
    If that fails, we approximate 1 token ≈ 4 characters.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except:
        return len(text) // 4  # Rough fallback estimate


class LLMProviders:
    """Manage OpenAI and Cohere with fallback."""

    def __init__(self):
        # Initialize OpenAI client using API key from Config
        self.openai_client = OpenAI(api_key=Config.OPENAI_API_KEY)

        # Initialize Cohere V2 client
        self.cohere_client = cohere.ClientV2(Config.COHERE_API_KEY)

        # Initialize cost tracker
        self.cost_tracker = CostTracker()

        # --- Rate limiting setup ---
        # Store last time each provider was called
        self.openai_last_call = 0
        self.cohere_last_call = 0

        # Minimum interval between calls (seconds)
        self.openai_interval = 60.0 / Config.OPENAI_RPM
        self.cohere_interval = 60.0 / Config.COHERE_RPM

    def _wait_openai(self):
        """
        Ensure we don't exceed OpenAI rate limits.
        """
        elapsed = time.time() - self.openai_last_call
        if elapsed < self.openai_interval:
            time.sleep(self.openai_interval - elapsed)

        self.openai_last_call = time.time()

    def _wait_cohere(self):
        """
        Ensure we don't exceed Cohere rate limits.
        """
        elapsed = time.time() - self.cohere_last_call
        if elapsed < self.cohere_interval:
            time.sleep(self.cohere_interval - elapsed)

        self.cohere_last_call = time.time()

    def ask_openai(self, prompt):
        """
        Send a prompt to OpenAI and return the response text.
        """
        self._wait_openai()

        # Count input tokens for cost estimation
        input_tokens = count_tokens(prompt)

        # Send chat completion request
        response = self.openai_client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract response text
        output_text = response.choices[0].message.content

        # Count output tokens
        output_tokens = count_tokens(output_text)

        # Track cost
        self.cost_tracker.track_request(
            "openai",
            Config.OPENAI_MODEL,
            input_tokens,
            output_tokens,
        )

        # Ensure we stay within daily budget
        self.cost_tracker.check_budget(Config.DAILY_BUDGET)

        return output_text

    def ask_cohere(self, prompt):
        """
        Send a prompt to Cohere (V2 API) and return the response text.
        """
        self._wait_cohere()

        # Count input tokens
        input_tokens = count_tokens(prompt)

        # Send chat request to Cohere
        response = self.cohere_client.chat(
            model=Config.COHERE_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        # Cohere V2 response structure:
        # response.message.content is a list → extract text
        output_text = response.message.content[0].text

        # Count output tokens
        output_tokens = count_tokens(output_text)

        # Track cost
        self.cost_tracker.track_request(
            "cohere",
            Config.COHERE_MODEL,
            input_tokens,
            output_tokens,
        )

        # Check budget
        self.cost_tracker.check_budget(Config.DAILY_BUDGET)

        return output_text

    def ask_with_fallback(self, prompt, primary="openai"):
        """
        Try primary provider first.
        If it fails, automatically fallback to the other provider.
        """
        try:
            if primary == "openai":
                print("Trying OpenAI (primary)...")
                return {
                    "provider": "openai",
                    "response": self.ask_openai(prompt)
                }
            else:
                print("Trying Cohere (primary)...")
                return {
                    "provider": "cohere",
                    "response": self.ask_cohere(prompt)
                }

        except Exception as e:
            print(f"Primary provider failed: {e}")
            print("Falling back...")

            # Switch provider automatically
            if primary == "openai":
                return {
                    "provider": "cohere",
                    "response": self.ask_cohere(prompt)
                }
            else:
                return {
                    "provider": "openai",
                    "response": self.ask_openai(prompt)
                }
