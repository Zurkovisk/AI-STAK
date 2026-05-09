#!/usr/bin/env bash

PROMPT="$*"
MODEL="qwen2.5-coder:7b"

SYSTEM="Você é um especialista Linux.

IMPORTANTE:
- responda SOMENTE com um comando shell válido
- nunca explique
- nunca use markdown
- nunca use crases
- use comandos modernos Linux
- prefira ss em vez de netstat
- o comando deve funcionar no zsh"

JSON=$(jq -n \
  --arg model "$MODEL" \
  --arg prompt "$SYSTEM

Usuário: $PROMPT" \
  '{
    model: $model,
    prompt: $prompt,
    stream: false
  }')

RAW=$(curl -s http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "$JSON")

CMD=$(echo "$RAW" | jq -r '.response')

# limpeza
CMD=$(echo "$CMD" | sed 's/```//g')
CMD=$(echo "$CMD" | sed 's/`//g')
CMD=$(echo "$CMD" | head -n 1)
CMD=$(echo "$CMD" | xargs)

# bloqueios de segurança
if [[ "$CMD" == "bash" ]]; then
  echo "❌ comando bloqueado"
  exit 1
fi

if [[ "$CMD" == "zsh" ]]; then
  echo "❌ comando bloqueado"
  exit 1
fi

if [[ "$CMD" == "sh" ]]; then
  echo "❌ comando bloqueado"
  exit 1
fi

# substituições inteligentes
if [[ "$CMD" == *"netstat"* ]]; then
  CMD="ss -tulnp"
fi

# corrigir awk sem quotes
CMD=$(echo "$CMD" | sed -E "s/awk \\{([^}]*)\\}/awk '{\\1}'/g")
# fallback inteligente
if [[ "$PROMPT" == *"portas abertas"* ]]; then
  CMD="ss -tulnp"
fi

echo "$CMD"
