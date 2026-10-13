import requests

def test_baidu_status():
    """验证百度首页能正常访问"""
    r = requests.get("https://www.baidu.com", timeout=5)
    assert r.status_code == 200

def test_math():
    """简单断言测试"""
    assert 1 + 1 == 2

def test_string():
    """字符串校验"""
    assert "jenkins" in "jenkins ci"