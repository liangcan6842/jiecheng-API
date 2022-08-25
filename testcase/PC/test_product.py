import pytest,requests,json
def test_1_add_product_type(get_token_fixture):
    """添加产品分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "level": 1,
        "name": "测试产品分类",
        "status": 1
    }
    url = "http://jiecheng.api.sauou.com/erp-admin-api/v1/category"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_add_product(get_token_fixture):
    """添加产品"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "unitPrice": 12,
            "image": "测试图片8-25",
            "quantity": 20,
            "color": "绿色",
            "unitName": "测试单位8-25实业集团",
            "density": 5,
            "level": 1,
            "colorId": 2,
            "weight": 10,
            "checkWeight": 1,
            "categoryName": "五金材料",
            "volume": 4,
            "specs": "2*10",
            "name": "三开开关",
            "unitId": 2,
            "categoryId": 15,
            "status": 1
    }
    url = "http://jiecheng.api.sauou.com/erp-admin-api/v1/product"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()