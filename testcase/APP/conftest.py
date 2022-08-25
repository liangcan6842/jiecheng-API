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
    url = "http://jiecheng.api.sauou.com/sys-app-api/v1/a/login"
    data = {
        "username": "test",
        "password": "123456"
    }
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    token = res["data"]
    return token