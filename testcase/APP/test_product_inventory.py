import requests,json,pytest
URL = "http://192.168.110.173:9100"
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
    url = URL + "http://192.168.110.173:9100/erp-app-api/v1/a/ps/in"
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
    url = URL + "http://192.168.110.173:9100/erp-app-api/v1/a/ps/in/record"
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
    url = URL + "http://192.168.110.173:9100/erp-app-api/v1/a/ps/in/detail"
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
        "code": "7628ee8b-4f22-4f15-b087-242af930417c",
        "lineId": 1,
        "keeps": [
            {
                "quantity": 15,
                "weight": 11,
                "productKeepId": 3
            }
        ],
        "outType": 1  #(1:再生产,2:订单出库)
    }
    url = URL + "http://192.168.110.173:9100/erp-app-api/v1/a/ps/out"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_out_storage_record(get_token_fixture):
    """产品入库记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "limit":"10",
            "page":"1"
    }
    url = URL + "http://192.168.110.173:9100/erp-app-api/v1/a/ps/out/record"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_out_storage_record_detail(get_token_fixture):
    """产品入库记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "id":"5"
    }
    url = URL + "http://192.168.110.173:9100/erp-app-api/v1/a/ps/out/detail"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()
