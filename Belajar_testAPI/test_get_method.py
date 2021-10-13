import requests
import pytest

def test_get_method():
    url = 'https://reqres.in/api/users/2'
    response = requests.get(url)

    Code = response.status_code

    assert Code == 201