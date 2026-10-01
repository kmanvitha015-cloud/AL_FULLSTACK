import chromadb
import streamlit as it
from ollama import chat
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Technova concierge", page_icon=".", layout = "wide")

st.cache_resource
def load_resources():
    model = sentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.persistentclient(path="chroma_db")
    collection = client.get_or_create_collection('fest_docs')
    return model, collection

model, collection = load_resources()

st.title("🎪 Nova, the Technova concierge")
st.caption("I only know about the fest documents. Ask me anything about Technova!")
