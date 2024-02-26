# GTA V Review Chatbot

## Project Overview

This project develops an interactive chatbot designed to field questions about GTA V, drawing directly from user reviews. By harnessing advanced NLP techniques and machine learning models—including LangChain, OpenAI's GPT, and AstraDB's vector database—the chatbot delivers insightful responses on gameplay experiences, player feedback, and much more.

## Features

- **Personalized Responses**: Generates tailored answers from a dataset of GTA V Steam reviews.
- **Retrieval-Augmented Generation (RAG)**: Leverages RAG to provide contextually relevant responses.
- **Vector Database Integration**: Utilizes AstraDB for efficient retrieval of vector embeddings.
- **Interactive UI**: Features a user-friendly interface powered by Streamlit, enhancing user interaction.

## Implementation Steps

1. **Initialization**:
    - Created accounts and generated API keys/tokens on AstraDB and OpenAI.
2. **Data Preparation and Indexing**:
    - Initialized my AstraDB vector database and populated it with GTA review data. This included generating vector embeddings using LangChain and OpenAI (see `gta_v_review_analysis.ipynb` for details).
3. **Chatbot Development**:
    - Developed an OpenAI-powered chatbot that indexes the newly added data, generating responses specific to the dataset and user inquiries.