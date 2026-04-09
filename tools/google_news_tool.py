import feedparser
from langchain.tools import tool
from config import MAX_ARTICLES_PER_SOURCE

@tool
def fetch_from_google_news(query: str) -> str:
    """Fetch news articles from Google News RSS feed for  given search query.
    Returns a list of articles with title, description, url, and source."""

    try:
        query_encoded = query.replace(" ","+")
        url = f"https://news.google.com/rss/search?q={query_encoded}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        
        articles = []
        for entry in feed.entries[:MAX_ARTICLES_PER_SOURCE]:
            articles.append({
                "title": entry.get("title",""),
                "description": entry.get("summary",""),
                "url": entry.get("link",""),
                "source": "Google News",
                "publishedAt": entry.get("published",""),
            })
        return articles
    except Exception as e:
        return [{"error": str(e)}]