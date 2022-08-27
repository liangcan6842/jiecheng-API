import requests,json,pytest
def test_1_add_waste(get_token_fixture):
    """新增废料"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "colorId": 1,
        "name": "LED屏",
        "weight": 1,
        "lineId": 1
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/wst/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_select_waste(get_token_fixture):
    """产品入库"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1"
    }
    url = "http://192.168.110.173:9100/erp-app-api/v1/a/wst/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()
