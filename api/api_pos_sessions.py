import setting
from setting import KFPT_IP, PORT1, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiPosSessions:
    '''
    获取当前登录用户信息接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取当前登录用户信息接口的url地址：')
        # 构造url地址
        self.url = KFPT_IP + ':' + PORT1 + '/pm-oauth/pos/sessions'
        logger.info('获取当前登录用户信息接口的url地址为：{}'.format(self.url))

    def pos_session(self, session):
        # 入参
        params = {'access_token': setting.access_token}  # 调用配置文件中的access_token
        logger.info('准备发起获取当前登录用户信息接口的请求，请求的header是：{},请求的参数是：{}'.format(HEADERS, params))
        # 发起请求
        response = session.get(self.url, params=params, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        logger.info('准备获取响应值的pos_id')
        # 获取响应值中的pos_id
        setting.pos_id = response.json().get('pos_id')  # 产生数据，并把数据放到setting当中
        setting.district_id = response.json().get('district_id')
        logger.info('获取的pos_id是：{}'.format(setting.pos_id))
        return response
