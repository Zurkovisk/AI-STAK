import chromadb
import ollama
import sys

client = chromadb.PersistentClient(path="./memory")
collection = client.get_or_create_collection("terminal")

text = sys.argv[1]

embedding = ollama.embeddings(
    model='nomic-embed-text',
    prompt=text
)

collection.add(
    ids=[str(hash(text))],
    documents=[text],
    embeddings=[embedding['embedding']]
)

print('memorizado')
