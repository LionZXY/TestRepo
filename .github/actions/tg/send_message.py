import requests
import os


payload = {'chat_id': os.environ['CHAT_ID'], 'parse_mode': 'markdown', 'disable_web_page_preview': true, 'text': os.environ['TEXT']} 
url = 'https://api.telegram.org/bot'+ os.environ['TG_TOKEN'] + '/sendMessage'
print(payload)
print(url)

response = requests.post('https://api.telegram.org/bot'+ os.environ['TG_TOKEN'] + '/sendMessage', data = payload)
print(response)
