from os import read
import requests
import json
import pytest
import jsonpath

def test_update():
    url = 'https://api.trello.com/1/boards/'
    file = open('c:/Users/hp/PycharmProjects/Belajar_testAPI/post.json', 'r')
    requests_json =json.loads(file.read())
    response = requests.post(url,json=requests_json)
    Code = response.status_code
    assert Code == 200
    json_response = json.loads(response.text)
    Name = jsonpath.jsonpath(json_response, 'name')
    assert Name[0] == 'Test via pytest Baru nih'