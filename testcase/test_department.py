import pytest,requests,json

# def test_1_add_department(get_token_fixture):
#     """增加部门信息"""
#     # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
#     headers = {
#         "Content-Type": "application/json;charset=utf8",
#         "Authorization": get_token_fixture
#     }
#     data = {
#             "createTime": "",
#             "sortNumber": 1,
#             "name": "测试部门3",
#             "checked": "true",
#             "updateTime": "",
#             "shortName": "测试部",
#             "status": 1
#     }
#     url = "http://192.168.110.173:9000/sys-admin-api/v1/department"
#     res = requests.post(url=url, headers=headers, json=data).text
#     res = json.loads(res)
#     print(res)
#     assert res["code"] == 200

def test_2_select_department(get_token_fixture):
    """查询部门信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = "http://192.168.110.173:9000/sys-admin-api/v1/department/all/tree"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()
