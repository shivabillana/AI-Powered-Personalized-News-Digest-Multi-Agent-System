from agents.graph import run_graph


def run_digest(topics: list[str], keywords: list[str]) -> dict:
    """
    LangGraph-based orchestrator

    For each topic:
    - Runs the LangGraph workflow
    - Returns structured 

    Output:
    {
        topic: {
            "digest" : str,
            "articles" : list
        }
    }
    """
    results = {}

    for topic in topics:
        print(f"\n[Orchestrator] Processing: {topic}")

        result = run_graph(topic,keywords)

        results[topic] = {
            "digest": result.get("digest",""),
            "articles": result.get("filtered_articles",[]),
        }

    return results