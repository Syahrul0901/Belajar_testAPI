from os import read
import requests
import json
import pytest
import jsonpath

def test_update():
    url = 'https://api.trello.com/1/board/6166ce6c8f63cd81e0fe8a5e'
    file = open('c:/Users/hp/PycharmProjects/Belajar_testAPI/post.json', 'r')
    requests_json =json.loads(file.read())
    response = requests.put(url,json=requests_json)
    Code = response.status_code
    assert Code == 200
    json_response = json.loads(response.text)
    Name = jsonpath.jsonpath(json_response, 'name')
    assert Name[0] == 'Daily work day 3'
