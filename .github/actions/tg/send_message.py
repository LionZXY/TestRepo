import http.client
import json
import os

url = 'https://enlesz7htgigo.x.pipedream.net/bot'+ os.environ['TG_TOKEN'] + '/sendMessage'
payload = {'chat_id': os.environ['CHAT_ID'], 'parse_mode': 'markdown', 'disable_web_page_preview': True, 'text': os.environ['TEXT']} 
json_payload =  json.dumps(payload).encode('utf8')

print(json_payload)
print(url)

conn = http.client.HTTPSConnection('api.telegram.org')
conn.request("POST", '/bot'+ os.environ['TG_TOKEN'] + '/sendMessage', json_payload, {'Content-Type': 'application/json'})
print(conn.getresponse())
