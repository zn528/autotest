'''
金融项目充值测试：注册用户-->登录-->充值1000
'''
import pytest

from zonghe.baw import Member, Operate
from zonghe.caw import DataRead


@pytest.fixture(DataRead.read_yaml(r"test_data\recharge_data.yaml"))
def recharge_data(request):
    return request.param

def recharge(recharge_data,baserequest,url,data):
    # 注册用户
    Member.register(baserequest,url,recharge_data['regdata'])
    # 登录用户
    Member.login(baserequest,url,recharge_data['logindata'])
    # 充值界面
    r = Operate.recharge(baserequest,url,recharge_data['rechargedata'])
    print(r.text)
    # 验证充值返回结果
    # 删除登录用户