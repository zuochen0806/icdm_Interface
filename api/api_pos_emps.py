import setting
from setting import KFPT_IP, PORT2, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiPosEmps:
    '''
    获取医卫人员信息
    '''

    def __init__(self):
        # 构造url地址
        logger.info('开始获医卫人员信息的url地址：')
        self.url = KFPT_IP + ':' + PORT2 + '/OpenPlatformService/public/pos/emps'
        logger.info('获取医卫人员信息的地址是{}'.format(self.url))

    def pos_emps(self, session):
        # 入参
        params = {'access_token': setting.access_token,  # 调用配置文件中的access_token
                  'pos_id': setting.pos_id  # 调用配置文件中的pos_id
                  }
        logger.info('准备发起获取医卫人员信息的请求，请求的参数是{}，header是{}'.format(params, HEADERS))
        # 发起请求
        response = session.get(self.url, params=params, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是{}'.format(response))
        return response
