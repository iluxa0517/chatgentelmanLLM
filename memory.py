import chromadb

client = chromadb.PersistentClient(path="data/memory")
collection = client.get_or_create_collection("chat_memory")

def add_memory(text, metadata=None):
    collection.add(
        documents=[text],
        ids=[str(hash(text))],
        metadatas=[metadata or {}]
    )

def search(query, n_results=5):
    res = collection.query(query_texts=[query], n_results=n_results)
    return res['documents'][0]
