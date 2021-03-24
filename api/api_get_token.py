import setting
from setting import KFPT_IP, PORT1, HEADERS, grant_type, client_id, client_secret
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiGetToken:
    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取token的url地址：')
        # 构造url地址
        self.url = KFPT_IP + ':' + PORT1 + '/pm-oauth/oauth/token'
        logger.info('获取token的url地址为：{}'.format(self.url))

    def get_token(self, session, data):
        '''
        todo 对获取token接口进行自动化操作，并根据响应获取返回值中的”access_token“值
        data: 动态传参，由于用户名和密码是动态的其他参数都是固定的，这里只需要动态传用户名和密码
        '''
        # 入参
        params = {'grant_type': grant_type,
                  'username': data['username'],
                  'password': data['password'],
                  'client_id': client_id,
                  'client_secret': client_secret
                  }
        logger.info('准备发起获取token的请求，请求的header是：{},请求的参数是：{}'.format(HEADERS, params))
        logger.info('请求的用户名是：{},请求的密码是：{}'.format(data['username'], data['password']))
        # 发起请求
        response = session.get(self.url, params=params, headers=HEADERS)
        logger.info('获取的响应值是：{}'.format(response))
        logger.info('准备获取响应值的token')
        # 获取响应值中的access_token
        setting.access_token = response.json().get('access_token')  # 产生数据，并把数据放到setting当中
        logger.info('获取的token是：{}'.format(setting.access_token))
        return response

    def get_token_success(self, session):
        '''
        todo 获取token成功接口，用于关联其他接口
        '''
        # 入参
        params = {'grant_type': 'password',
                  'username': 'xiang01',
                  'password': '123456',
                  'client_id': '8b38b6f11f894b7498fd92d52ef276c7',
                  'client_secret': '9bc555f6b3224cf3a600206008e2b4d2'
                  }
        logger.info('准备发起获取token的请求，请求的header是：{},请求的参数是：{}'.format(HEADERS, params))
        logger.info('请求的用户名是：{},请求的密码是：{}'.format(params['username'], params['password']))
        # 发起请求
        response = session.get(self.url, params=params, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        logger.info('准备获取响应值的token')
        # 获取响应值中的access_token
        setting.access_token = response.json().get('access_token')  # 产生数据，并把数据放到setting当中
        logger.info('获取的token是：{}'.format(setting.access_token))
        return response


if __name__ == '__main__':
    import requests

    ApiGetToken().get_token_success(session=requests.session())
