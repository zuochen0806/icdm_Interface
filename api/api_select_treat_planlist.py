import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiSelectTreatPlanlist:
    '''
    查询治疗方案列表接口（分页）
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<查询治疗方案列表接口（分页）>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/treatPlan/selectTreatPlanList/'
        logger.info('<查询治疗方案列表接口（分页）>的url地址为：{}'.format(self.url))

    def select_treat_planlist(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        data = {'planName': '',
                'diseaseType': '',
                'pageNo': 1,
                'pageSize': 20}
        logger.info('准备发起<查询治疗方案列表接口（分页）>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.get(self.url, json=data, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        setting.datas = response.json().get('result')['datas']
        return response
