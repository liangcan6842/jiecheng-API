import pytest,requests,json
def test_1_add_information(get_token_fixture):
    """新增消息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "read": 1,
        "resType": 1,
        "name": "纸巾",
        "title": "新增订单消息",
        "userId": 1,
        "resId": 2,
        "content": "你的订单已开始处理，等待商家发货",
        "outInId": 3,
        "status": 1
    }
    url = "http://jiecheng.api.sauou.com/erp-admin-api/v1/sysMessage"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_select_information(get_token_fixture):
    """查询消息详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":"9"}
    url = "http://jiecheng.api.sauou.com/erp-admin-api/v1/sysMessage"
    res = requests.get(url=url, headers=headers,params =data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_select_page_information(get_token_fixture):
    """查询消息详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"page":"1","limit":"10"}
    url = "http://jiecheng.api.sauou.com/erp-admin-api/v1/sysMessage/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()



