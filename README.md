---

# 📰 AI-Powered Personalized News Digest (v2.0)

An **AI agent-based news intelligence system** that fetches, filters, and summarizes news articles into a personalized digest.

Built with **LangChain**, **LangGraph**, **LangSmith**, **OpenRouter**, and **Streamlit**.

---

## 🚀 Features

✅ Fetches news from multiple sources (**NewsAPI + Google News**)
✅ Uses **LLM-powered filtering** to rank article relevance
✅ Removes duplicate/noisy articles
✅ Generates structured topic-wise news digests
✅ Interactive **Streamlit UI**
✅ **LangGraph-powered workflow orchestration**
✅ **LangSmith tracing for debugging & observability**
✅ **Evaluation pipeline** for measuring agent performance

---

# 🧠 Version Evolution

| Version  | Description                                             |
| -------- | ------------------------------------------------------- |
| **v1.0** | Basic multi-agent pipeline → Fetch → Filter → Summarize |
| **v2.0** | Added LangGraph workflow control                        |
| **v2.1** | Added LangSmith tracing/debugging                       |
| **v2.2** | Added evaluation framework for measuring agent quality  |

---

# 🏗️ System Architecture

### Before (v1)

```text
User Input → Fetch → Filter → Summarize → UI
```

---

### Current Architecture (v2.2)

```text
User Input
   ↓
LangGraph Orchestrator
   ↓
Fetch Node
   ↓
Filter Node
   ↓
Summarize Node
   ↓
Streamlit UI

        +
LangSmith Tracing
        +
Evaluation Framework
```

---

# 🤖 Agents / Nodes

---

## 1. Fetch Agent

**Type:** Python Tool Layer

Responsibilities:

* Fetch articles from NewsAPI
* Fetch articles from Google News
* Merge results

---

## 2. Filter Agent

**Type:** LLM Agent

Responsibilities:

* Score article relevance
* Remove duplicates
* Rank top articles

---

## 3. Summarizer Agent

**Type:** LLM Agent

Responsibilities:

* Generate concise digest
* Highlight key developments
* Provide article summaries

---

## 4. LangGraph Controller

**Type:** Workflow Layer

Responsibilities:

* Controls execution flow
* Maintains shared state
* Coordinates nodes

---

# 🔍 LangSmith Observability

Integrated **LangSmith** for:

* Execution tracing
* Llm call debugging
* Token monitoring
* Latency tracking
* Failure analysis

Example trace:

```text
run_graph
 ├── fetch_node
 ├── filter_node
 └── summarize_node
```

---

# 📊 Evaluation Framework

Built an evaluation pipeline to measure agent performance.

### Evaluation Flow

```text
Test Dataset → Agent → Llm Judge → Score → Results
```

### Metrics

* Relevance
* Clarity
* Coverage

### Current Average Score

**7.5/10**

---

# 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* LangSmith
* OpenRouter
* Streamlit
* NewsAPI
* Google News RSS

---

# 📂 Project Structure

```bash
news-project/
│
├── app.py
├── graph.py
├── evaluation.py
├── config.py
│
├── agents/
│   ├── orchestrator.py
│   ├── fetcher.py
│   ├── filter.py
│   ├── summarizer.py
│
├── tools/
│   ├── newsapi_tool.py
│   ├── google_news_tool.py
│
└── README.md
```

---

# ⚙️ Installation

```bash
git clone <your_repo_url>
cd news-project
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
NEWSAPI_KEY=your_key
OPENROUTER_API_KEY=your_key
OPENROUTER_MODEL=your_model

LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=news-agent
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Run Evaluation

```bash
python evaluation.py
```

---

# Future Improvements

* Retry mechanisms
* Memory for tracking long-term trends
* Multi-agent collaboration
* Personalized recommendations
* Real-time alerts

---

# Key Learning Outcomes

This project helped me learn:

✅ Multi-agent systems
✅ LangGraph orchestration
✅ LangSmith debugging
✅ LLM evaluation pipelines
✅ Production-style AI workflows

---

## Final Outcome

This project evolved from a simple news summarizer into a **production-style AI agent system** focused on:

**Control → Observability → Evaluation**

## 👤 Author

1. Shiva Kumar Billana

2. Nithin Chandra
