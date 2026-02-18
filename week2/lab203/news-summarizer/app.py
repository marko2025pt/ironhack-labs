"""
Streamlit Web Interface for News Summarizer

This file creates a simple web-based GUI so we can:
- Select news category
- Choose number of articles
- Run the summarizer
- See summaries and sentiment
- Run unit tests from the browser
"""

import streamlit as st
import subprocess
from summarizer import NewsSummarizer


# -----------------------------
# Page Configuration
# -----------------------------
# This sets the browser tab title and page layout
st.set_page_config(page_title="News Summarizer", layout="wide")

# Main title displayed at top of the page
st.title("📰 Multi-Provider News Summarizer")


# -----------------------------
# Sidebar Configuration Panel
# -----------------------------
# Sidebar is used for user controls

st.sidebar.header("Configuration")

# Dropdown menu for selecting news category
category = st.sidebar.selectbox(
    "Select News Category",
    ["technology", "business", "health", "general"]
)

# Slider to choose how many articles to process
num_articles = st.sidebar.slider(
    "Number of Articles",
    min_value=1,
    max_value=5,
    value=2
)

# Button to run the summarizer
run_button = st.sidebar.button("Run Summarizer")

# Button to run unit tests
run_tests_button = st.sidebar.button("Run Unit Tests")


# -----------------------------
# Run Summarizer Section
# -----------------------------
# This block runs when the user clicks "Run Summarizer"

if run_button:
    st.subheader("Fetching and Processing Articles...")

    # Create summarizer object
    summarizer = NewsSummarizer()

    # Fetch articles from NewsAPI
    articles = summarizer.news_api.fetch_top_headlines(
        category=category,
        max_articles=num_articles
    )

    # If no articles returned, show error
    if not articles:
        st.error("No articles found.")
    else:
        # Process articles (summary + sentiment)
        results = summarizer.process_articles(articles)

        # Display each article result
        for result in results:
            st.markdown("---")

            # Article title
            st.subheader(result["title"])

            # Basic metadata
            st.write(f"**Source:** {result['source']}")
            st.write(f"**Published:** {result['published_at']}")

            # Clickable link
            st.write(f"[Read full article]({result['url']})")

            # Summary section
            st.markdown("### Summary")
            st.write(result["summary"])

            # Sentiment section
            st.markdown("### Sentiment")
            st.write(result["sentiment"])

        # -----------------------------
        # Cost Summary Section
        # -----------------------------
        cost_summary = summarizer.llm_providers.cost_tracker.get_summary()

        st.markdown("---")
        st.subheader("💰 Cost Summary")

        st.write(f"Total Requests: {cost_summary['total_requests']}")
        st.write(f"Total Cost: ${cost_summary['total_cost']:.6f}")

        total_tokens = (
            cost_summary['total_input_tokens'] +
            cost_summary['total_output_tokens']
        )

        st.write(f"Total Tokens: {total_tokens}")


# -----------------------------
# Run Unit Tests Section
# -----------------------------
# This block runs when user clicks "Run Unit Tests"

if run_tests_button:
    st.subheader("Running Unit Tests...")

    # Run pytest as a subprocess (separate process)
    result = subprocess.run(
        ["pytest", "-v"],
        capture_output=True,
        text=True
    )

    # If returncode is 0 → tests passed
    if result.returncode == 0:
        st.success("All tests passed!")
    else:
        st.error("Some tests failed.")

    # Display full pytest output
    st.text(result.stdout)
