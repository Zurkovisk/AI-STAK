import subprocess

def analyze_log(log):
    prompt = f"""
Analise este log e detecte anomalias ou ataques:

{log}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3:8b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout