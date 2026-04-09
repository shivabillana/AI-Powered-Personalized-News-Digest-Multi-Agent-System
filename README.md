# 📰 AI-Powered Personalized News Digest

A multi-agent news intelligence system that fetches, filters, and summarizes news articles into a clean, personalized digest.

Built using **LangChain**, **OpenRouter (LLMs)**, and **Streamlit**.

---

## 🚀 Features

* 🔍 Fetches news from multiple sources (NewsAPI + Google News)
* 🎯 Filters and ranks articles using LLM-based relevance scoring
* ✍️ Generates clean, structured summaries
* 🧠 Multi-agent architecture (Fetcher → Filter → Summarizer)
* ⚡ Fast and scalable pipeline
* 🎨 Interactive Streamlit UI

---

## 🧩 Architecture

```
User Input → Fetch (Python) → Filter (LLM) → Summarize (LLM) → UI
```

### Agents:

* **Fetcher (Python)** → Collects raw articles
* **Filter Agent (LLM)** → Scores relevance & removes duplicates
* **Summarizer Agent (LLM)** → Creates readable digest

---

## 📸 Output

* Topic-wise digest
* Key highlights
* Article summaries
* Source links with relevance scores

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenRouter (LLMs)
* Streamlit
* NewsAPI
* Google News

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/news-digest.git
cd news-digest
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENROUTER_API_KEY=your_key
OPENROUTER_MODEL=your_model
NEWSAPI_KEY=your_newsapi_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters topics and keywords
2. System fetches news from APIs
3. LLM filters and ranks articles
4. LLM generates a clean digest
5. Results displayed in UI

---

## ⚡ Performance Optimizations

* Parallel processing for topics
* Reduced token usage
* Deduplication before LLM
* Caching support

---

## 💼 Use Cases

* Personalized news dashboards
* AI-powered research tools
* Content aggregation systems
* Daily news automation

---

## 📌 Future Improvements

* LangGraph workflow
* Real-time streaming updates
* Vector DB (RAG memory)
* Sentiment analysis
* Deployment (AWS / Render)

---

## 👨‍💻 Author

Shiva Kumar Billana

Nithin Chandra Maddi

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
