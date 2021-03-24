import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiSelectUseMedicineById:
    '''
    根据治疗方案id查询治疗方案详情接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<根据治疗方案id查询治疗方案详情接口>的url地址：')
        treatmentPlanId = setting.datas[0]['treatmentPlanId']
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/treatPlan/selectUseMedicineById/' + treatmentPlanId
        logger.info('<根据治疗方案id查询治疗方案详情接口>的url地址为：{}'.format(self.url))

    def select_use_medicine_byid(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        logger.info('准备发起<根据治疗方案id查询治疗方案详情接口>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.get(self.url, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response
