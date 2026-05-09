#!/usr/bin/env bash

PROMPT="$*"

if [[ ${#PROMPT} -lt 80 ]]; then
  MODEL="qwen2.5-coder:7b"
else
  MODEL="devstral-small-2"
fi

curl -s http://localhost:11434/api/generate \
-d "{
  \"model\": \"$MODEL\",
  \"prompt\": \"$PROMPT\",
  \"stream\": false
}" | jq -r '.response'
