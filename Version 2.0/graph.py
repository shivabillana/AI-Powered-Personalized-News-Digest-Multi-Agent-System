from langgraph.graph import StateGraph
from agents.fetcher_copy import fetch as fetch_articles
from agents.filter import filter_articles
from agents.summarizer import summarize_articles

def create_initial_state(topic: str,keywords: list[str])-> dict:
    return {
        "topic" : topic,
        "keywords" : keywords,
        "articles" : [],
        "filtered_articles" : [],
        "digest" : ""
    }

def fetch_node(state: dict)-> dict:
    print("[Graph] Fetching...")
    articles = fetch_articles(state["topic"])
    state["articles"] = articles
    return state

def filter_node(state: dict)-> dict:
    print("[Graph] Filtering...")
    filtered = filter_articles(
        state["articles"],
        state["topic"],
        state["keywords"]
    )
    state["filtered_articles"] = filtered
    return state

def summarize_node(state: dict) -> dict:
    print("[Graph] Summarizing...")
    digest = summarize_articles(
        state["filtered_articles"],
        state["topic"]
        )
    
    state["digest"] = digest
    return state

def build_graph():
    builder = StateGraph(dict)

    builder.add_node("fetch",fetch_node)
    builder.add_node("filter", filter_node)
    builder.add_node("summarize",summarize_node)

    builder.set_entry_point("fetch")

    builder.add_edge("fetch","filter")
    builder.add_edge("filter","summarize")

    return builder.compile()

graph = build_graph()

def run_graph(topic: str, keywords: list[str]) -> dict:
    state = create_initial_state(topic, keywords)
    result = graph.invoke(state)
    return result

