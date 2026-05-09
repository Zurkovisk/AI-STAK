import subprocess

print("🔍 Lint")
subprocess.run(["flake8", "../workspace"])

print("🛡️ Security")
subprocess.run(["bandit", "-r", "../workspace"])