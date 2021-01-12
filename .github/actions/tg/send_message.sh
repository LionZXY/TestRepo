#!/bin/bash

json_escape () {
    printf '%s' "$1" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))'
}

LOCAL_TG_TOKEN=$(json_escape $TG_TOKEN)
LOCAL_CHAT_ID=$(json_escape $CHAT_ID)
LOCAL_TEXT=$(json_escape $TEXT)
echo $LOCAL_TG_TOKEN
echo $LOCAL_CHAT_ID
echo $LOCAL_TEXT
echo $CHAT_ID


curl -X POST \
    -H 'Content-Type: application/json' \
    -d "{\"chat_id\": $LOCAL_CHAT_ID, \"parse_mode\":\"markdown\", \"disable_web_page_preview\":true, \"text\": $LOCAL_TEXT}" \
    "https://api.telegram.org/bot$TG_TOKEN/sendMessage"
