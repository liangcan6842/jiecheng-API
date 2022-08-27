import requests,json,pytest
def test_1_storage(get_token_fixture):
    """产品入库"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "truckId": 6,
        "code": "1ef18c26f0b6",
        "lineId": 1,
        "keeps": [
            {
                "quantity": 20,
                "weight": 10,
                "productKeepId": 15
            }
        ],
        "inType": 2
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ps/in"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_storage_record(get_token_fixture):
    """产品入库记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "limit":"10",
            "page":"1",
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ps/in/record"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_storage_record_details(get_token_fixture):
    """产品入库详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "id":"5"
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ps/in/detail"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_out_storage(get_token_fixture):
    """产品出库"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "code": "c3164dbedd54",
        "lineId": 1,
        "keeps": [
            {
                "quantity": 15,
                "weight": 11,
                "productKeepId": 16
            }
        ],
        "outType": 1
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ps/out"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200




if __name__ == '__main__':
    pytest.main()
