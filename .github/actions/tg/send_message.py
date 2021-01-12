from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import os

url = 'https://enlesz7htgigo.x.pipedream.net/bot'+ os.environ['TG_TOKEN'] + '/sendMessage'
payload = {'chat_id': os.environ['CHAT_ID'], 'parse_mode': 'markdown', 'disable_web_page_preview': True, 'text': os.environ['TEXT']} 
json_payload =  json.dumps(payload).encode('utf8')

print(json_payload)
print(url)

request = Request('https://enlesz7htgigo.x.pipedream.net/', data=json_payload,
                 headers={'content-type': 'application/json'})
response = urlopen(request).read().decode('utf8')
print(response)
