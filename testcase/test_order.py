import pytest,requests,json
def test_1_add_order(get_token_fixture):
    """新增订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "productId": 10,
            "productCount": 100,
            "customId": 1
    }
    url = "http://192.168.110.173:9000/erp-admin-api/v1/order"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200












if __name__ == '__main__':
    pytest.main()