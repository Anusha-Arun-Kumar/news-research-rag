# News & Research RAG Assistant

## Overview

This project builds a **Retrieval-Augmented Generation (RAG)** system that answers questions using a large news dataset.

The system retrieves relevant articles using semantic search and generates answers using a Large Language Model.

Example question:

> What are the latest trends in artificial intelligence?

The system retrieves relevant news articles and generates a summarized answer with sources.

---

## Architecture

Dataset → Preprocessing → Chunking → Embeddings → Vector Database → Retriever → LLM → Streamlit UI

---

## Features

* Semantic search across thousands of news articles
* Retrieval-Augmented Generation (RAG)
* LLM-generated answers
* Source citations
* Interactive chat interface

---

## Tech Stack

Python
LangChain
FAISS Vector Database
OpenAI API
Streamlit

---

## Project Structure

news-research-rag
│
├── data/
├── notebooks/
├── src/
│   ├── ingest.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── app/
│   └── streamlit_app.py
│
└── README.md

---

## Example Query

User:
What are recent developments in generative AI?

Assistant:
Recent developments include diffusion models, multimodal systems, and improved model alignment techniques.

Sources:

* AI breakthroughs in generative models
* Advances in multimodal learning

---

## Dataset

HuffPost News Category Dataset from Kaggle.

Contains ~200k news articles across multiple categories.

---

## Future Improvements

* Live news ingestion using APIs
* Hybrid search (vector + keyword search)
* RAG evaluation metrics
* Docker deployment
