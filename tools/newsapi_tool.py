from langchain.tools import tool
from newsapi import NewsApiClient
from config import NEWSAPI_KEY, MAX_ARTICLES_PER_SOURCE

@tool
def fetch_from_newsapi(query: str) -> str:
    """Fetch top news articles from NewsAPI for a given search query.
    Return a list of articles with title, description, url, and source."""

    try:
        client = NewsApiClient(api_key=NEWSAPI_KEY)
        response = client.get_everything(
            q = query,
            language = 'en',
            sort_by = 'relevancy',
            page_size = MAX_ARTICLES_PER_SOURCE
        )
        articles = []
        for a in response.get("articles",[]):
            articles.append({
                "title": a.get("title",""),
                "description": a.get("description",""),
                "url":a.get("url",""),
                "source": a.get("source",{}).get("name","NewsAPI"),
                "publishedAt": a.get("publishedAt",""),
            })

        return articles
    except Exception as e:
        return [{"error": str(e)}]