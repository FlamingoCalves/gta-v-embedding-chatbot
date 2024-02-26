# initialization.py
from langchain_community.llms import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from config import ASTRA_DB_API_ENDPOINT, ASTRA_DB_TOKEN, OPENAI_API_KEY

def init_services():
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    myEmbeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vstore = AstraDBVectorStore(
        embedding=myEmbeddings,
        collection_name="gta_reviews",
        token=ASTRA_DB_TOKEN,
        api_endpoint=ASTRA_DB_API_ENDPOINT,
    )
    vectorIndex = VectorStoreIndexWrapper(vectorstore=vstore)
    return llm, myEmbeddings, vstore, vectorIndex
