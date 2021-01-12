import http.client
import json
import os


text = os.environ['TEXT']
print(text)
payload = {'chat_id': os.environ['CHAT_ID'], 'parse_mode': 'markdown', 'disable_web_page_preview': True, 'text': str(text)} 
json_payload =  json.dumps(payload).encode('utf8')

print(json_payload)

conn = http.client.HTTPSConnection('api.telegram.org')
conn.request("POST", '/bot'+ os.environ['TG_TOKEN'] + '/sendMessage', json_payload, {'Content-Type': 'application/json'})
response = conn.getresponse()
print(json.loads(response.read().decode()))
