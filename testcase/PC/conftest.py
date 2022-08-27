import pytest
import requests
import json

@pytest.fixture(scope="session")
def get_token_fixture():
    '''
    作用域为session的fixture函数，返回token
    :return:
    '''
    headers = {"Content-Type": "application/json;charset=utf8"}
    url = "http://192.168.110.173:9100/sys-admin-api/v1/login"
    data = {
        "username": "admin",
        "password": "123456"
    }
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    token = res["data"]
    return token