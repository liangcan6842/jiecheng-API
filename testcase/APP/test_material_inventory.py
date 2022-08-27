import requests,json,pytest
def test_1_storage(get_token_fixture):
    """材料入库"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "fromType": 2,      #1:本厂,2:外场
        "keeps": [
            {
                "materialKeepId": 123496   #材料实例ID
            }
        ],
        "inType": 1      #1原材料，2再生料
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ms/in"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_storage_record(get_token_fixture):
    """材料入库记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "limit":"10",
            "page":"1",
            "name":"",
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ms/in/record"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_storage_record_details(get_token_fixture):
    """材料入库详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "id":"5"
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ms/in/detail"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_out_storage(get_token_fixture):
    """材料出库"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "lineId": 0,  #生产线ID
            "keeps": [
                {
                    "materialKeepId": 123496  #材料实例ID
                }
            ]
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/ms/out"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200




if __name__ == '__main__':
    pytest.main()
