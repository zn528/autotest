import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySQLOp


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param

def test_login(login_data,baserequest,url,db_info):
    # 注册用户
    print("注册数据",login_data['regdata'])
    r = Member.register(baserequest,url,login_data['regdata'])
    # 登录
    print("登录数据", login_data['logindata'])
    r = Member.login(baserequest, url, login_data['logindata'])
    # 检查结果
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']
    # 删除注册用户
    MySQLOp.delete_user(db_info, login_data['regdata']['mobilephone'])