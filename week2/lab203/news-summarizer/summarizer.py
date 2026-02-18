"""News summarizer with multi-provider support."""
# This file orchestrates the whole pipeline:
# 1. Fetch news articles
# 2. Summarize them with OpenAI
# 3. Analyze sentiment with Cohere
# 4. Generate a final report

from news_api import NewsAPI
from llm_providers import LLMProviders


class NewsSummarizer:
    """Summarize news articles using multiple LLM providers."""

    def __init__(self):
        # Create instances of the API modules
        # NewsAPI → fetches raw news
        # LLMProviders → handles OpenAI + Cohere
        self.news_api = NewsAPI()
        self.llm_providers = LLMProviders()

    def summarize_article(self, article):
        """
        Process a single article:
        - Generate summary (OpenAI primary, Cohere fallback)
        - Analyze sentiment (Cohere)
        """

        # Print first 60 characters of title for tracking progress
        print(f"\nProcessing: {article['title'][:60]}...")

        # Build a formatted text block to send to the LLM
        # We limit content length to avoid excessive token cost
        article_text = f"""Title: {article['title']}
Description: {article['description']}
Content: {article['content'][:500]}"""

        # ---------------------------
        # Step 1: Summarization
        # ---------------------------
        # We use OpenAI as primary because it is cheaper/faster
        try:
            print("  => Summarizing with OpenAI...")

            # Prompt instructing the model what to do
            summary_prompt = f"""Summarize this news article in 2-3 sentences:

{article_text}"""

            # Call OpenAI through provider abstraction
            summary = self.llm_providers.ask_openai(summary_prompt)

            print("  Summary generated")

        except Exception as e:
            # If OpenAI fails → automatically fallback to Cohere
            print(f"  OpenAI failed: {e}")
            print("  → Falling back to Cohere...")

            summary = self.llm_providers.ask_cohere(summary_prompt)

        # ---------------------------
        # Step 2: Sentiment Analysis
        # ---------------------------
        # We use Cohere for sentiment (better nuance)
        try:
            print("  => Analyzing sentiment with Cohere...")

            sentiment_prompt = f"""Analyze the sentiment of this text:

"{summary}"

Provide:
- Overall sentiment (positive/negative/neutral)
- Confidence (0-100%)
- Key emotional tone

Be concise (2-3 sentences)."""

            # Call Cohere
            sentiment = self.llm_providers.ask_cohere(sentiment_prompt)

            print("  Sentiment analyzed")

        except Exception as e:
            # If sentiment fails, don't crash whole pipeline
            print(f"  Sentiment analysis failed: {e}")
            sentiment = "Unable to analyze sentiment"

        # Return structured result dictionary
        return {
            "title": article["title"],
            "source": article["source"],
            "url": article["url"],
            "summary": summary,
            "sentiment": sentiment,
            "published_at": article["published_at"],
        }

    def process_articles(self, articles):
        """
        Process a list of articles sequentially.
        If one fails, continue with the rest.
        """
        results = []

        for article in articles:
            try:
                result = self.summarize_article(article)
                results.append(result)

            except Exception as e:
                # Prevent entire batch from failing due to one article
                print(f" Failed to process article: {e}")

        return results

    def generate_report(self, results):
        """
        Print a formatted console report showing:
        - Article summaries
        - Sentiment analysis
        - Cost statistics
        """

        print("\n" + "=" * 80)
        print("NEWS SUMMARY REPORT")
        print("=" * 80)

        # Print each processed article
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   Source: {result['source']} | Published: {result['published_at']}")
            print(f"   URL: {result['url']}")

            print("\n   SUMMARY:")
            print(f"   {result['summary']}")

            print("\n   SENTIMENT:")
            print(f"   {result['sentiment']}")

            print(f"\n   {'-'*76}")

        # Get cost summary from CostTracker
        summary = self.llm_providers.cost_tracker.get_summary()

        print("\n" + "=" * 80)
        print("COST SUMMARY")
        print("=" * 80)

        print(f"Total requests: {summary['total_requests']}")
        print(f"Total cost: ${summary['total_cost']:.6f}")
        print(f"Total tokens: {summary['total_input_tokens'] + summary['total_output_tokens']:,}")

        print("=" * 80)


# This allows the file to run directly for manual testing.
# It will not run when imported from another module.
if __name__ == "__main__":

    summarizer = NewsSummarizer()

    print("Fetching news articles...")

    # Fetch 2 technology articles
    articles = summarizer.news_api.fetch_top_headlines(
        category="technology",
        max_articles=2
    )

    # Only process if articles were successfully fetched
    if articles:
        print(f"\n Processing {len(articles)} articles...")

        results = summarizer.process_articles(articles)

        summarizer.generate_report(results)
