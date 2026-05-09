from langchain.llms import Ollama

llm = Ollama(model="llama3:8b")

goal = "Automatizar deploy de um projeto Python com testes e segurança"

context = ""

while True:
    prompt = f"""
Objetivo: {goal}
Contexto atual: {context}

Qual próximo passo executar?
Responda com:
AÇÃO: <comando ou tarefa>
"""

    response = llm.invoke(prompt)
    print(response)

    action = input("Executar? (y/n): ")
    if action == "y":
        context += response