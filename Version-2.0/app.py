import streamlit as st
from agents.orchestrator import run_digest

st.set_page_config(
    page_title="Personalized News Digest",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Personalized News Digest")
st.caption("Powered by LangChain agents + OpenRouter")

# --- Sidebar ---
with st.sidebar:
    st.header("Your Preferences")

    topics_input = st.text_area(
        "Topics (one per line)",
        placeholder="Artificial Intelligence\nPython\nSpace Exploration",
        height=150,
    )

    keywords_input = st.text_input(
        "Extra keywords (comma separated)",
        placeholder="LLM, open source, NASA",
    )

    st.divider()
    run_btn = st.button("Generate Digest", type="primary", use_container_width=True)

# --- Main Area ---
if run_btn:
    topics = [t.strip() for t in topics_input.strip().splitlines() if t.strip()]
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

    if not topics:
        st.warning("Please enter at least one topic.")
    else:
        st.info(f"Generating digest for: **{', '.join(topics)}**... this may take a minute.")

        with st.spinner("Agents are working..."):
            results = run_digest(topics, keywords)

        st.success("✅ Digest ready!")
        st.divider()

        for topic, data in results.items():
            with st.expander(f"📌 {topic}", expanded=True):

                st.markdown(data["digest"])

                if data["articles"]:
                    st.markdown("#### 🔗 Sources")
                    for article in data["articles"]:
                        score = article.get("score", "")
                        score_badge = f" `{score:.2f}`" if isinstance(score, float) else ""
                        st.markdown(
                            f"- [{article.get('title', 'No title')}]({article.get('url', '#')}) "
                            f"— *{article.get('source', '')}*{score_badge}"
                        )
else:
    st.markdown("""
    ### How it works
    1. Enter your topics in the sidebar
    2. Optionally add keywords to narrow focus
    3. Click **Generate Digest**

    **Three agents will work together:**
    - 🔍 **Fetcher agent** — searches NewsAPI + Google News
    - 🎯 **Filter agent** — scores and ranks by relevance
    - ✍️ **Summarizer agent** — writes a clean digest per topic
    """)