from crewai import Agent, Task, Crew
from langchain.llms import Ollama

llm_code = Ollama(model="deepseek-coder:6.7b")
llm_chat = Ollama(model="llama3:8b")

coder = Agent(
    role="Senior Developer",
    goal="Escrever código limpo e funcional",
    backstory="Especialista em backend e scripts",
    llm=llm_code
)

reviewer = Agent(
    role="Code Reviewer",
    goal="Revisar e melhorar código",
    backstory="Focado em qualidade e segurança",
    llm=llm_chat
)

task1 = Task(
    description="Criar um script Python que monitora CPU",
    agent=coder
)

task2 = Task(
    description="Revisar o script e sugerir melhorias",
    agent=reviewer
)

crew = Crew(
    agents=[coder, reviewer],
    tasks=[task1, task2]
)

print(crew.run())

from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

emb = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(persist_directory="./vector_db", embedding_function=emb)