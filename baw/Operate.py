'''业务操作'''

# 充值
def recharge(baserequest,url,data):
    url = url + 'futureloan/mvc/api/member/recharge'
    r = baserequest.post(url,data=data)
    return r