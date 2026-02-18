"""Configuration management for news summarizer."""
# This file centralizes all configuration values (API keys, models, limits, etc.)
# so the rest of the application can import them from one place.

import os
from dotenv import load_dotenv

# Load environment variables from the .env file into the system environment.
# This allows us to use os.getenv() to access them.
load_dotenv()


class Config:
    """Application configuration."""
    # This class stores all configuration values as class attributes.
    # We access them using Config.VARIABLE_NAME anywhere in the project.

    # -----------------------
    # API Keys
    # -----------------------
    # These values are read from the .env file.
    # If they don't exist, they will return None.
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    # -----------------------
    # Environment
    # -----------------------
    # If ENVIRONMENT is not defined in .env,
    # it defaults to "development".
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    # -----------------------
    # API Configuration
    # -----------------------
    # Maximum number of retries if an API call fails.
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

    # Timeout (in seconds) for API requests.
    # If a request takes longer than this, it will fail.
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))

    # -----------------------
    # Models
    # -----------------------
    # OpenAI model used for summarization.
    OPENAI_MODEL = "gpt-4o-mini"

    # Cohere model used for sentiment analysis (V2 API model).
    COHERE_MODEL = "command-a-03-2025"

    # -----------------------
    # Cost Control
    # -----------------------
    # Maximum daily budget allowed for API usage (in USD).
    DAILY_BUDGET = float(os.getenv("DAILY_BUDGET", "5.00"))

    # -----------------------
    # Rate Limits (requests per minute)
    # -----------------------
    # These values help us avoid hitting provider rate limits.
    OPENAI_RPM = 500
    COHERE_RPM = 100
    NEWS_API_RPM = 100

    @classmethod
    def validate(cls):
        """
        Validate that required configuration is present.

        This method checks whether all required API keys exist.
        If any are missing, the program will stop with an error.
        """
        required = [
            ("OPENAI_API_KEY", cls.OPENAI_API_KEY),
            ("COHERE_API_KEY", cls.COHERE_API_KEY),
            ("NEWS_API_KEY", cls.NEWS_API_KEY),
        ]

        # Build a list of missing keys
        missing = [name for name, value in required if not value]

        # If at least one required key is missing → stop execution
        if missing:
            raise ValueError(
                f"Missing required configuration: {', '.join(missing)}"
            )

        # If everything is fine → print confirmation
        print(f"Configuration validated for {cls.ENVIRONMENT} environment")


# Validate configuration automatically when this file is imported.
# This ensures the app never runs with missing API keys.
Config.validate()
