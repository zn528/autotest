'''断言'''
import pytest_check as check
def equal(real,expect,keys):
    '''
        assert r.json()['code'] == fail_data['expect']['code']
        assert r.json()['status'] == fail_data['expect']['status']
        assert r.json()['msg'] == fail_data['expect']['msg']
        简化为Check.equal(r.json(),fail_data['expect'],'code,status,msg')
        检查两个字典中，key对应的value是否一致
        不推荐直接判等 r.json() == fail_data['expect']
        1.结果中有一些不关键信息，后面有变化时，会导致脚本执行不通过
        2.结果中有时间戳这类变化的信息，每次校验的结果不同，需要变更数据，比如查询所有用户当中包含时间戳
        3.结果可能很长，顺序发生变化，不方便维护。比如查询所有用户，数据量10w
        :param real:实际结果，字典格式的
        :param expect:预期结果的，字典格式的
        :param keys:对比的key
        :return:
     '''
    ks = keys.split(",")
    for k in ks:
        r = str(real.get(k))   # 根据k取实际结果中的value
        e = str(expect.get(k))  # 根据k取预期结果中的value
        # r =str(real[k])
        # e = str(expect[k])
        try:
            check.equal(r,e)
            print(f"校验{k}成功")
        except Exception as e:
            print(f"校验{k}失败")


