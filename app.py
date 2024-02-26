# app.py
import streamlit as st
from initialization import init_services
from response_generation import get_response

llm, myEmbeddings, vstore, vectorIndex = init_services()

st.title('GTA V Review Chatbot')

user_question = st.text_input("Enter your question about GTA V reviews:")

if st.button('Get Answer') or user_question:
    answer, docs_by_relevance = get_response(user_question, vectorIndex, vstore, llm)
    st.write("ANSWER:", answer)
    st.write("DOCUMENTS BY RELEVANCE:")
    for doc, score in docs_by_relevance:
        st.write(f"Score: {score:.4f} - Document: \"{doc.page_content[:60]}...\"")