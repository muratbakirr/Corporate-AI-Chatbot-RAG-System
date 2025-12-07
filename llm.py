""" Loading LLM and embedding """

from langchain_ollama import ChatOllama, OllamaEmbeddings
#from langchain_community.embeddings import CacheBackedEmbeddings   # removed
#from langchain_community.storage import LocalFileStore

chat_model = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
    max_tokens=None
)

base_embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest"
)

# # Cache embeddings --- Saves embeddings to disk, avoids recomputing
# store = LocalFileStore("./cache/")

# EMBEDDINGS = CacheBackedEmbeddings.from_bytes_store(
#     base_embeddings,
#     store,
#     namespace="nomic-embed-text",
# )