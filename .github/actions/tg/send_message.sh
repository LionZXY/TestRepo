#!/bin/bash

TOKEN=$1
CHAT_ID=$2
TEXT=$3

curl -X POST \
    -H 'Content-Type: application/json' \
    -d "{\"chat_id\": \"$CHAT_ID\", \"text\": \"$TEXT\"}" \
    "https://api.telegram.org/bot$TOKEN/sendMessage"
