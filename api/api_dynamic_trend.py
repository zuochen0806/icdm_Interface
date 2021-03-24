import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiDynamicTrend:
    '''
    查询患者动态趋势分布接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<查询患者动态趋势分布接口>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/dataBoard/patientDynamicTrend/' + setting.district_id
        logger.info('<查询患者动态趋势分布接口>的url地址为：{}'.format(self.url))

    def dynamic_trend(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        logger.info('准备发起<查询患者动态趋势分布接口>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.get(self.url, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response
