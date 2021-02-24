'''
更灵活的一种测试前置和后置：fixture
    可以不使用setup、teardown的方式命名
    使用起来更灵活
'''
import pytest

# 测试前置：测试之前的环境准备、环境初始化、测试数据准备等
# 测试后置：测试结束后环境恢复等
# 前置后置可以直接使用参数的方式传参，也可以使用装饰器方法@pytest.mark.usefixtures('login')
@pytest.fixture(scope='function') #默认是function级别的
def login():
    print("登录系统")
    yield  #yield之前是前置，yield之后是后置
    print("退出系统")
    print("测试结束")

def test_query():
    print("查询功能，不需要登录")

def test_add(login):
    print("添加功能，需要登录")

@pytest.mark.usefixtures('login')
def test_delete():
    print("删除添加功能，需要登录")

def test_register():
    print("注册功能，不需要登录")