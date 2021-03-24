import os

# 开放平台IP
KFPT_IP = 'http://192.168.1.46'
JCGW_IP = 'http://192.168.8.230'
# 端口号
PORT1 = '8080'
PORT2 = '8081'
PORT3 = '8083'
# headers
HEADERS = {'X-Requested-With': 'XMLHttpRequest',
           'Content-Type': 'application/json'
           }
# 获取token接口入参
grant_type = 'password'
client_id = '8b38b6f11f894b7498fd92d52ef276c7'
client_secret = '9bc555f6b3224cf3a600206008e2b4d2'
# 获取绝对路径
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)
# 获取token接口返回之中的access_token
access_token = None  # 初始化动态产生的access_token数据
# 获取当前登录用户信息接口返回值中的pos_id
pos_id = None  # 初始化动态产生的pos_id数据
organizationId = None  # 初始化动态产生的organizationId数据
district_id = None  # 初始化动态产生的district_id数据
HEADER = {'access-token': access_token}
# 获取<查询治疗方案列表接口（分页）>接口返回值中的datas
datas = None
