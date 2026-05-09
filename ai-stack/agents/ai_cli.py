import subprocess
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def ask_ai(prompt):
    result = subprocess.run(
        ["ollama", "run", "deepseek-coder:6.7b"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout

def run_shell(cmd):
    subprocess.run(cmd, shell=True)

console.print("[bold green]AI Terminal iniciado[/bold green]")

while True:
    user_input = Prompt.ask("🤖")

    if user_input in ["exit", "quit"]:
        break

    if user_input.startswith("!"):
        run_shell(user_input[1:])
    else:
        response = ask_ai(user_input)
        console.print(f"[cyan]{response}[/cyan]")