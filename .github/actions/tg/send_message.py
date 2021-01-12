from urllib.request import Request, urlopen

url = 'https://api.telegram.org/bot'+ os.environ['TG_TOKEN'] + '/sendMessage'
payload = {'chat_id': os.environ['CHAT_ID'], 'parse_mode': 'markdown', 'disable_web_page_preview': true, 'text': os.environ['TEXT']} 

print(payload)
print(url)

request = Request(url, urlencode(payload).encode())
response = urlopen(request).read()
print(response)
