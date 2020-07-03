import requests

fields = {
    'token': 'REDCAPSECRETTOKEN',
    'content': 'metadata',
    'format': 'json',
    'returnFormat': 'json',
}

r = requests.post('https://redcap-api-end-point-url', fields)
with open('data-dict.json', 'w', encoding='utf-8') as fw:
    fw.write(r.text)
