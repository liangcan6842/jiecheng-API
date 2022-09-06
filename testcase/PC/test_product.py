import pytest,requests,json
URL = "http://192.168.110.173:9100"
def test_1_add_product_type(get_token_fixture):
    """添加产品分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "level": 3,
        "name": "产品分类827-等级3",
        "status": 1
    }
    url = URL + "/erp-admin-api/v1/category"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
    categoryId = res["data"]["id"]
    return categoryId

def test_2_add_product(get_token_fixture):
    """添加产品"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "unitPrice": 15,
        "image": "测试图片827-产线2",
        "quantity": 20,
        "unitName": "测试单位8-25实业集团",
        "density": 5,
        "level": 2,
        "colorId": 2,
        "weight": 10,
        "checkWeight": 1,
        "categoryName": "五金材料",
        "volume": 5,
        "specs": "2*10*12",
        "name": "测试产品827-产线2",
        "unitId": 3,
        "categoryId": 20,
        "status": 1
    }
    url = URL + "/erp-admin-api/v1/product"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_select_product(get_token_fixture):
    """分页查询产品"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "level": "1",
        "page": "1",
        "limit": "20",
        "name": "",
        "categoryId": ""
    }
    url = URL + "/erp-admin-api/v1/product"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_print_product_code(get_token_fixture):
    """打印产品码"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "productId": "11",
        "count": "1 "
    }
    url = URL + "/erp-admin-api/v1/product/QR"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()