import os
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

MAX_ARTICLES_PER_SOURCE = 5
MAX_ARTICLES_AFTER_FILTER = 8