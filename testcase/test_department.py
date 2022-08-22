import pytest,requests,json

def test_1_add_department(get_token_fixture):
    """增加部门信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "sortNumber": 1,
            "name": "测试部门8-22",
            "checked": "true",
            "shortName": "测试部",
            "status": 1
    }
    url = "http://192.168.110.173:9000/sys-admin-api/v1/department"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

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

def test_3_revise_department(get_token_fixture):
    """修改部门信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = "http://192.168.110.173:9000/sys-admin-api/v1/department"
    data ={
        "createTime": "",
        "sortNumber": 1,
        "name": "测试部门3",
        "checked": "true",
        "id": "42",
        "updateTime": "",
        "shortName": "测试部",
        "status": 1
    }
    res = requests.post(url=url, headers=headers,data=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


def test_4_delete_department(get_token_fixture):
    """删除部门信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = "http://192.168.110.173:9000/sys-admin-api/v1/departments/delete"
    data ={
        "id": '40',
        "syncDelete": 0
    }
    res = requests.post(url=url, headers=headers,data=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_add_user(get_token_fixture):
    """新增用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = "http://192.168.110.173:9000/sys-admin-api/v1/user/add"
    data ={
        "password": "123456",
        "gender": 1,
        "nickName": "lucky",
        "departmentId": 1,
        "mobile": "18875272418",
        "remark": "新增用户",
        "avatar": "2345",
        "username": "李四"
    }
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_select_user(get_token_fixture):
    """查询用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = "http://192.168.110.173:9000/sys-admin-api/v1/user/list"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200







if __name__ == '__main__':
    pytest.main()
