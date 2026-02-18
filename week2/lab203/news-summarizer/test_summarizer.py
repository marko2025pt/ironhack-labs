"""Unit tests for news summarizer."""
# This file contains automated tests that verify the correctness
# of individual components without calling real external APIs.

import pytest
from unittest.mock import Mock, patch
from news_api import NewsAPI
from llm_providers import LLMProviders, CostTracker, count_tokens
from summarizer import NewsSummarizer


# -----------------------------
# Test Cost Tracking Logic
# -----------------------------
class TestCostTracker:

    def test_track_request(self):
        # Create a new cost tracker instance
        tracker = CostTracker()

        # Simulate a request with 100 input tokens and 500 output tokens
        cost = tracker.track_request("openai", "gpt-4o-mini", 100, 500)

        # Cost should be positive
        assert cost > 0

        # Total cost should equal this single request
        assert tracker.total_cost == cost

        # Exactly one request should be stored
        assert len(tracker.requests) == 1

    def test_get_summary(self):
        tracker = CostTracker()

        # Simulate two different API calls
        tracker.track_request("openai", "gpt-4o-mini", 100, 200)
        tracker.track_request("cohere", "command-a-03-2025", 150, 300)

        # Get aggregated summary
        summary = tracker.get_summary()

        # Check totals are correct
        assert summary["total_requests"] == 2
        assert summary["total_cost"] > 0
        assert summary["total_input_tokens"] == 250
        assert summary["total_output_tokens"] == 500

    def test_budget_check(self):
        tracker = CostTracker()

        # Small cost should not raise error
        tracker.track_request("openai", "gpt-4o-mini", 100, 100)
        tracker.check_budget(10.00)

        # Force budget overflow manually
        tracker.total_cost = 15.00

        # Expect exception when budget exceeded
        with pytest.raises(Exception):
            tracker.check_budget(10.00)


# -----------------------------
# Test Token Counting
# -----------------------------
class TestTokenCounting:

    def test_count_tokens(self):
        text = "Hello, how are you?"

        # Count tokens using our helper function
        count = count_tokens(text)

        # Token count must be positive
        assert count > 0

        # Tokens should be fewer than character count
        # (because tokens are chunks, not individual characters)
        assert count < len(text)


# -----------------------------
# Test NewsAPI (Mocked)
# -----------------------------
class TestNewsAPI:

    # Patch requests.get so no real HTTP request is made
    @patch('news_api.requests.get')
    def test_fetch_top_headlines(self, mock_get):

        # Create fake API response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "articles": [
                {
                    "title": "Test Article",
                    "description": "Test description",
                    "content": "Test content",
                    "url": "https://example.com",
                    "source": {"name": "Test Source"},
                    "publishedAt": "2026-01-19"
                }
            ]
        }

        # Make requests.get return our fake response
        mock_get.return_value = mock_response

        api = NewsAPI()
        articles = api.fetch_top_headlines(max_articles=1)

        # Validate processed result
        assert len(articles) == 1
        assert articles[0]["title"] == "Test Article"
        assert articles[0]["source"] == "Test Source"


# -----------------------------
# Test LLMProviders (Mocked)
# -----------------------------
class TestLLMProviders:

    # Patch OpenAI and Cohere clients so no real API calls happen
    @patch('llm_providers.OpenAI')
    @patch('llm_providers.cohere.ClientV2')
    def test_ask_openai(self, mock_cohere, mock_openai_class):

        # Create fake OpenAI client
        mock_openai_client = Mock()

        # Fake OpenAI response structure
        mock_response = Mock()
        mock_response.choices = [
            Mock(message=Mock(content="Test response"))
        ]

        # When .create() is called → return fake response
        mock_openai_client.chat.completions.create.return_value = mock_response

        # Replace real OpenAI client with mock
        mock_openai_class.return_value = mock_openai_client

        # Cohere also mocked (not used in this test)
        mock_cohere.return_value = Mock()

        providers = LLMProviders()

        # Call method under test
        response = providers.ask_openai("Test prompt")

        # Ensure returned text matches mocked response
        assert response == "Test response"


# -----------------------------
# Test NewsSummarizer (Mocked LLM calls)
# -----------------------------
class TestNewsSummarizer:

    # Patch LLM methods so no real API calls occur
    @patch.object(LLMProviders, 'ask_openai')
    @patch.object(LLMProviders, 'ask_cohere')
    def test_summarize_article(self, mock_cohere, mock_openai):

        # Define fake outputs
        mock_openai.return_value = "Test summary"
        mock_cohere.return_value = "Neutral sentiment"

        summarizer = NewsSummarizer()

        # Fake article input
        article = {
            "title": "Test Article",
            "description": "Test description",
            "content": "Test content",
            "url": "https://example.com",
            "source": "Test Source",
            "published_at": "2026-01-19"
        }

        result = summarizer.summarize_article(article)

        # Validate pipeline result
        assert result["title"] == "Test Article"
        assert result["summary"] == "Test summary"
        assert result["sentiment"] == "Neutral sentiment"
