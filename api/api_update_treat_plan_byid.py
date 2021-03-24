import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiUpdateTreatPlanById:
    '''
    新增/编辑治疗方案接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<新增/编辑治疗方案接口>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/treatPlan/updateTreatPlanById/'
        logger.info('<新增/编辑治疗方案接口>的url地址为：{}'.format(self.url))

    def update_treat_plan_byid(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        data = {
            "diseaseType": "1",
            "planName": "测试治疗方案",
            "planDescription": "这个是测试的治疗方案",
            "dictMedicine": [
                {
                    "medicineId": "f60de0faef9f4acc953a137f57d8db61",
                    "medicineCode": "11602003",
                    "medicineName": "奎尼丁(口服常释剂型)",
                    "medicineChemicaName": "奎尼丁(口服常释剂型)",
                    "dose": "1粒",
                    "unit": "粒",
                    "isValidate": 1,
                    "isCancel": 0,
                    "createOrgId": "1",
                    "orgName": "1",
                    "creatorId": "1",
                    "creator": "1",
                    "createTime": "2020-10-22",
                    "modifiedOrgId": "1",
                    "modifiedOrgName": "1",
                    "modifierId": "1",
                    "modifier": "1",
                    "modifiedTime": "2020-10-22",
                    "drugUsageDosage": "每日一次"
                }
            ]
        }
        logger.info('准备发起<新增/编辑治疗方案接口>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.post(self.url, json=data, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response

