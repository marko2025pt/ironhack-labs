# Multi-Provider News Summarizer

A production-style news analytics application that fetches real news articles, generates AI-powered summaries, performs sentiment analysis, tracks API costs, and provides both CLI and web interfaces.

## Project Overview

This application simulates a real-world news analytics system that:

- Fetches live news articles from NewsAPI
- Uses OpenAI (gpt-4o-mini) for summarization
- Uses Cohere (command-a-03-2025, V2 API) for sentiment analysis
- Implements fallback logic between providers
- Tracks token usage and API cost
- Respects rate limits
- Includes full unit testing
- Provides both CLI and Streamlit Web GUI

The system is designed to be reliable, cost-aware, and modular.

## Architecture

```
User Interface
│
├── main.py (CLI)
├── app.py (Streamlit Web UI)
│
Business Logic
│
├── summarizer.py
│
External Integrations
│
├── news_api.py
├── llm_providers.py
│
Configuration
│
├── config.py
│
Testing
│
└── test_summarizer.py
```

## Setup Instructions
### 1. Clone Repository

git clone <your-repo-url>
cd news-summarizer

### 2️. Create Virtual Environment (Recommended)
```
conda create -n news-env python=3.11
conda activate news-env
```

### 3️. Install Dependencies
```
pip install -r requirements.txt
```

### 4️. Configure Environment Variables

Create a .env file:
```
OPENAI_API_KEY=your_openai_key
COHERE_API_KEY=your_cohere_key
NEWS_API_KEY=your_newsapi_key

ENVIRONMENT=development
MAX_RETRIES=3
REQUEST_TIMEOUT=30
DAILY_BUDGET=5.00
```

⚠️⚠️⚠️ Do not commit .env to GitHub.

##  How to Run
### Option 1 — CLI Version
```
python main.py
```

You will:

- Select category
- Choose number of articles
- View summaries + sentiment in terminal
- See cost summary

#### Example Execution Output

See `main_output.txt` for full CLI execution example.

### Option 2 — Web GUI (Streamlit)
```
streamlit run app.py
```

Features:

- Category selector
- Article count slider
- Run summarizer button
- Cost summary display
- Run unit tests button

## Running Tests
```
pytest -v
```

All tests should pass.

The tests include:

- Cost tracking validation
- Token counting
- News API mocking
- LLM provider mocking
- Full summarization pipeline test

No real API calls are made during testing.

### Test Results

See `pytest_results.txt` for full unit test output.

## Cost Tracking

Each LLM request:

- Counts input tokens
- Counts output tokens
- Calculates estimated cost
- Tracks total daily usage
- Stops execution if budget exceeded
- Warns when 90% of budget is reached

Example output:

COST SUMMARY
Total requests: 4
Total cost: $0.000541
Total tokens: 671

## Fallback Logic

If OpenAI fails during summarization:
→ Cohere automatically takes over.

If a provider fails:
→ The system switches to the secondary provider.

This improves reliability in production environments.

## External APIs Used

NewsAPI → https://newsapi.org

OpenAI → https://platform.openai.com

Cohere (V2 API) → https://dashboard.cohere.com



## What I Learned

- Multi-provider LLM integration
- Handling API rate limits
- Token counting and cost estimation
- Environment variable configuration
- Mocking external APIs in unit tests
- Designing modular architectures
- Implementing fallback reliability
- Building a simple Streamlit GUI

## Possible Improvements

- Add caching to avoid re-processing duplicate articles
- Store processed articles in a database
- Add async processing for higher throughput
- Deploy as a cloud web app
- Add more LLM providers (e.g., Gemini)
- Add trending topic detection
- Add email reporting

## Submission Checklist

- External API integration
- Multi-provider LLM usage
- Fallback logic
- Cost tracking
- Rate limiting
- Unit tests passing
- Clean configuration management
- No API keys committed
- CLI + Web Interface

## Reflection

One of the first challenges I faced was integrating the News API correctly. Initially, I was using credentials from a different provider (newsapi.ai instead of newsapi.org), which resulted in persistent 401 Unauthorized errors. This forced me to carefully review the API documentation, confirm the correct base URL, and ensure that the API key matched the expected service. It reinforced the importance of validating external dependencies early and understanding exactly which service endpoint is being used.

A second challenge involved Cohere model compatibility. Several models referenced in older documentation (e.g., command-r and command-light) had been deprecated, which caused 404 errors. I resolved this by switching to the Cohere V2 client and updating the model to command-a-03-2025, adapting the response parsing accordingly. This experience highlighted how quickly AI APIs evolve and the importance of verifying current model availability rather than relying on outdated examples.

Another practical issue arose when exporting CLI output to log files. Windows PowerShell raised encoding errors due to Unicode characters (✓, ✗) in log messages. Removing those characters ensured compatibility with file redirection and made the application more production-robust.

Through this project, I also learned how pytest discovers tests automatically by looking for files and functions prefixed with “test,” and how mocking allows external APIs to be simulated during unit testing. Additionally, building both a CLI and a Streamlit GUI helped me understand the difference between command-line interaction (using input()) and event-driven web interfaces, and how to separate business logic from presentation layers.

For improvement, I would add caching to prevent reprocessing duplicate articles, implement asynchronous calls for scalability, and deploy the Streamlit interface to a cloud environment.

## Final Result

A production-(almost) ready, modular, cost-aware AI news summarization system with testing and web interface.