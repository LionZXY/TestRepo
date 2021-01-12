from urllib.request import Request, urlopen
import os

url = 'https://api.telegram.org/bot'+ os.environ['TG_TOKEN'] + '/sendMessage'
payload = {'chat_id': os.environ['CHAT_ID'], 'parse_mode': 'markdown', 'disable_web_page_preview': True, 'text': os.environ['TEXT']} 

print(payload)
print(url)

request = Request(url, urlencode(payload).encode())
response = urlopen(request).read()
print(response)
