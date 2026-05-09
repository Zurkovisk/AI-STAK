import os
import subprocess

def generate_tests(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Arquivo não encontrado: {file_path}")
        return

    with open(file_path, "r") as f:
        code = f.read()

    prompt = f"""


Gere testes pytest completos para este código:

{code}
"""

    result = subprocess.run(
        ["ollama", "run", "deepseek-coder:6.7b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    test_file = file_path.replace(".py", "_test.py")

    with open(test_file, "w") as f:
        f.write(result.stdout)

    print(f"✅ Testes criados: {test_file}")

def run_tests():
    subprocess.run(["pytest"])

if __name__ == "__main__":
    generate_tests("main.py")
    run_tests()