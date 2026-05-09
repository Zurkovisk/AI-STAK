import subprocess

def run_security_checks():
    print("🔍 Rodando lint...")
    subprocess.run(["flake8", "."])

    print("🛡️ Rodando análise de segurança...")
    subprocess.run(["bandit", "-r", "."])

def ai_review():
    with open("main.py") as f:
        code = f.read()

    prompt = f"""
Analise este código para vulnerabilidades e melhorias de segurança:

{code}
"""

    subprocess.run(
        ["ollama", "run", "llama3:8b"],
        input=prompt,
        text=True
    )

run_security_checks()
ai_review()