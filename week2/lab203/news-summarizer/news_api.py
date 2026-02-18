"""News API integration module."""
# This file is responsible for communicating with the external NewsAPI service.
# It fetches real news articles that we later summarize and analyze.

import requests
import time
from config import Config


class NewsAPI:
    """Fetch news articles from NewsAPI."""

    def __init__(self):
        # Store API key from configuration
        self.api_key = Config.NEWS_API_KEY

        # Base URL for NewsAPI endpoints
        self.base_url = "https://newsapi.org/v2"

        # Used to control rate limiting (avoid too many requests per minute)
        self.last_call_time = 0

        # Minimum time (in seconds) between API calls
        # Example: if limit is 100 requests per minute,
        # then we must wait 0.6 seconds between calls.
        self.min_interval = 60.0 / Config.NEWS_API_RPM  # Rate limiting

    def _wait_if_needed(self):
        """Wait if we need to rate limit."""
        # Calculate how much time passed since last API call
        elapsed = time.time() - self.last_call_time

        # If not enough time has passed → wait
        if elapsed < self.min_interval:
            wait_time = self.min_interval - elapsed
            print(f"Rate limiting News API: waiting {wait_time:.2f}s...")
            time.sleep(wait_time)

        # Update last call time
        self.last_call_time = time.time()

    def fetch_top_headlines(self, category="technology", country="us", max_articles=5):
        """
        Fetch top headlines from NewsAPI.

        Parameters:
        - category: News category (e.g., technology, business, health)
        - country: Country code (e.g., us, gb)
        - max_articles: Number of articles to retrieve

        Returns:
            List of simplified article dictionaries
        """

        # Ensure we respect rate limits before calling API
        self._wait_if_needed()

        # Build endpoint URL
        url = f"{self.base_url}/top-headlines"

        # Query parameters sent to NewsAPI
        params = {
            "apiKey": self.api_key,
            "category": category,
            "country": country,
            "pageSize": max_articles,
        }

        try:
            # Send GET request with timeout protection
            response = requests.get(
                url,
                params=params,
                timeout=Config.REQUEST_TIMEOUT
            )

            # Raise error if HTTP status is 4xx or 5xx
            response.raise_for_status()

            # Convert response JSON into Python dictionary
            data = response.json()

            # Check if NewsAPI returned an error status
            if data.get("status") != "ok":
                raise Exception(f"News API error: {data.get('message')}")

            # Extract list of articles
            articles = data.get("articles", [])

            # Clean and simplify article structure
            processed_articles = []

            for article in articles:
                processed_articles.append({
                    # Use .get() to avoid KeyError if field is missing
                    "title": article.get("title", ""),
                    "description": article.get("description", ""),
                    "content": article.get("content", ""),
                    "url": article.get("url", ""),
                    "source": article.get("source", {}).get("name", "Unknown"),
                    "published_at": article.get("publishedAt", "")
                })

            print(f"Fetched {len(processed_articles)} articles from News API")

            return processed_articles

        except requests.exceptions.RequestException as e:
            # Catch network errors, timeouts, invalid responses, etc.
            print(f"Error fetching news: {e}")
            return []


# This block allows the file to be run directly for testing.
# It will NOT run if the file is imported by another module.
if __name__ == "__main__":
    api = NewsAPI()

    # Fetch 3 technology articles for quick testing
    articles = api.fetch_top_headlines(category="technology", max_articles=3)

    # Print basic article information
    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']}")
        print(f"   URL: {article['url']}")
