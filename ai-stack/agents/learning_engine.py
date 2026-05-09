from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

emb = OllamaEmbeddings(model="nomic-embed-text")
db = Chroma(persist_directory="./memory", embedding_function=emb)

def learn_from_file(path):
    with open(path) as f:
        db.add_texts([f.read()])
    db.persist()

def ask_context(question):
    return db.similarity_search(question)