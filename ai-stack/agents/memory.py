import chromadb

client = chromadb.PersistentClient(path="./memory")

collection = client.get_or_create_collection("project")

def remember(text):
    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )

def search(query):
    return collection.query(
        query_texts=[query],
        n_results=3
    )

remember("Projeto usa FastAPI")

print(search("Qual framework usamos?"))