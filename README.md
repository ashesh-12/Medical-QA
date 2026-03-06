# 🏥 Medical QA — AI-Powered Medical Assistant

A Retrieval-Augmented Generation (RAG) based medical chatbot that helps general users understand diseases and symptoms. Built using **The Gale Encyclopedia of Medicine (2nd Edition)** as its knowledge base.

**🔗 Live Demo:** [medical-qa-rnip.onrender.com](https://medical-qa-rnip.onrender.com)

---

## What It Does

- Ask about any **disease** — get a clear, encyclopedia-backed explanation
- Describe your **symptoms** — get insights into what conditions could be related
- Designed for **general users** who want reliable medical information in plain language

> ⚠️ This is an informational tool only. Always consult a qualified medical professional for diagnosis and treatment.

---

## How It Works

The system follows a standard RAG pipeline:

1. **Data Extraction** — PDF pages extracted from The Gale Encyclopedia of Medicine
2. **Chunking** — Text split into 500-character chunks with 20-character overlap
3. **Embeddings** — Text chunks converted into vectors using `fastembed` (`all-MiniLM-L6-v2`)
4. **Vector Storage** — Embeddings stored and indexed in **Pinecone**
5. **Retrieval** — At query time, the user's question is embedded and matched against stored vectors
6. **Generation** — Relevant chunks passed to **Groq (LLaMA 3.3 70B)** to generate a natural language response

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Embeddings | FastEmbed (`all-MiniLM-L6-v2`) |
| Vector Database | Pinecone |
| LLM | Groq — LLaMA 3.3 70B Versatile |
| Orchestration | LangChain |
| Deployment | Render |

---

## Project Structure

```
Medical-QA/
├── src/
│   ├── helper.py         # Embedding model and PDF loading utilities
│   └── prompt.py         # System prompt for the LLM
├── static/               # CSS and frontend assets
├── templates/
│   └── chat.html         # Chat UI
├── data/                 # Source PDF data
├── research/             # Notebooks and experimentation
├── app.py                # Main Flask application
├── store_index.py        # One-time script to index data into Pinecone
├── requirements.txt      # Python dependencies
└── .env                  # API keys (not committed)
```

---

## Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Medical-QA.git
cd Medical-QA
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the app

```bash
python app.py
```

Visit `http://localhost:8000` in your browser.

---

## Environment Variables

| Variable | Description |
|---|---|
| `PINECONE_API_KEY` | Your Pinecone API key |
| `GROQ_API_KEY` | Your Groq API key |

---

## Data Source

**The Gale Encyclopedia of Medicine, 2nd Edition** — a comprehensive medical reference covering hundreds of diseases, conditions, symptoms, and treatments written for general audiences.

---

## Deployment

This app is deployed on **Render** (free tier). Note that on the free tier, the app sleeps after 15 minutes of inactivity — the first request after idle may take 30-60 seconds to respond while the server wakes up.