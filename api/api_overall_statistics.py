import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiOverallStatistics:
    '''
    查询慢病患者总体统计接口（地图）
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<查询慢病患者总体统计接口（地图）>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/dataBoard/patientOverallStatistics/' + setting.district_id
        logger.info('<查询慢病患者总体统计接口（地图）>的url地址为：{}'.format(self.url))

    def overall_statistics(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        logger.info('准备发起<查询慢病患者总体统计接口（地图）>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.get(self.url, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response
