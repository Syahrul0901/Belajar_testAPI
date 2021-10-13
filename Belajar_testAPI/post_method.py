from os import read
import requests
import json

url = 'https://api.trello.com/1/boards/'

file = open('c:/Users/hp/PycharmProjects/Belajar_testAPI/post.json', 'r')

requests_json =json.loads(file.read())

response = requests.post(url,json=requests_json)

# cetak response code 

print(response.status_code)

# cetak json file
json_response = json.loads(response.text)

print(json_response)