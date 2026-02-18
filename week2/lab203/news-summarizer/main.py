"""
Main application entry point.

This file allows the user to run the news summarizer
directly from the terminal (CLI version).
"""

import sys
from summarizer import NewsSummarizer


def main():
    """
    Main program flow:
    1. Ask user for configuration
    2. Fetch news articles
    3. Summarize + analyze sentiment
    4. Print report
    """

    print("=" * 80)
    print("NEWS SUMMARIZER - Multi-Provider Edition")
    print("=" * 80)

    # -----------------------------
    # User Input Section
    # -----------------------------

    # Ask for category (default = technology)
    category = input(
        "\nEnter news category (technology/business/health/general): "
    ).strip()

    # If user presses Enter → use default
    if not category:
        category = "technology"

    # Ask for number of articles
    num_articles_input = input("How many articles to process? (1-10): ").strip()

    try:
        # Convert input to integer
        num_articles = int(num_articles_input)

        # Clamp value between 1 and 10
        num_articles = max(1, min(10, num_articles))

    except ValueError:
        # If invalid input → default to 3
        num_articles = 3

    print(f"\n Fetching {num_articles} articles from category: {category}")

    try:
        # -----------------------------
        # Initialize summarizer
        # -----------------------------
        summarizer = NewsSummarizer()

        # Fetch articles from NewsAPI
        articles = summarizer.news_api.fetch_top_headlines(
            category=category,
            max_articles=num_articles
        )

        # Only continue if articles were fetched
        if articles:
            print(f"\n Processing {len(articles)} articles...")

            # Run summarization + sentiment pipeline
            results = summarizer.process_articles(articles)

            # Print final report
            summarizer.generate_report(results)

        else:
            print("No articles found. Please check your API key or category.")

        print("\n Processing complete!")

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\n Operation cancelled by user.")
        sys.exit(0)

    except Exception as e:
        # Catch unexpected errors
        print(f"\n Error: {e}")
        sys.exit(1)


# ---------------------------------
# This ensures the file only runs
# when executed directly:
#
# python main.py
#
# It will NOT run if imported.
# ---------------------------------
if __name__ == "__main__":
    main()
