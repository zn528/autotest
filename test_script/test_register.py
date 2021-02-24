'''
测试注册的脚本
'''
import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySQLOp, Check


@pytest.fixture(params=DataRead.read_yaml(r"test_data\register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"test_data\register_sucess.yaml"))
def sucess_data(request):
    return request.param

def test_register_fail(fail_data,baserequest,url):
    '''
    注册失败的脚本
    :return:
    '''
    print(fail_data)
    # 下发请求
    r = Member.register(baserequest,url,fail_data['data'])
    print(r.text)
    # 检查结果与预期结果一致
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['status'] == fail_data['expect']['status']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # 重复的代码，出现次数多的代码，可以封装成方法，简化调用
    Check.equal(r.json(),fail_data["expect"],"code,status,msg")

def test_register_sucess(sucess_data,baserequest,url,db_info):
    '''
    注册成功的脚本
    :param sucess_data:
    :param baserequest:
    :param url:
    :return:
    '''
    # print(sucess_data)
    # 初始化环境：避免环境中已有本次测试用到的数据
    MySQLOp.delete_user(db_info,sucess_data['data']['mobilephone'])
    # 下发请求
    r = Member.register(baserequest,url,sucess_data['data'])
    # 检查接口的返回结果与预期一致
    assert r.json()['code'] == sucess_data['expect']['code']
    assert r.json()['status'] == sucess_data['expect']['status']
    assert r.json()['msg'] == sucess_data['expect']['msg']
    # 检查用户在系统中测试成功(1.该用户可以登录成功 2.数据库中查有没有这个用户
    # 3、list接口返回值中是否能查到这个用户)
    r = Member.list(baserequest,url)
    assert sucess_data['data']['mobilephone'] in r.text
    # 清理环境：删除用户(1.接口删除用户  2.数据库删除用户)
    MySQLOp.delete_user(db_info,sucess_data['data']['mobilephone'])

    # 自动化测试原则1：测试环境在执行前是什么状态，执行完脚本要恢复到原来的状态。(清理环境)
    # 原则2：脚本执行依赖的环境，要在脚本中自己构造。
    # 比如：审核项目接口测试时依赖已有的项目，需要先调用添加项目的接口准备测试环境
    # 脚本的健壮性、稳定性较高
    # 原则3：脚本与脚本之间不要有依赖关系。脚本积累多了，依赖关系乱，无法确定哪些先执行，哪些后执行。

def test_register_repeat(repeat_data,baserequest,url,db_info):
    # 重复注册测试逻辑123456

    # 下发注册请求
    # 下发注册请求（检查测试结果，报错重复注册）
    # 恢复环境：删除注册用户
    pass
