import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiHyperConfirm:
    '''
    实时同步高血压确诊接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取实时同步高血压确诊接口的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/yfrhApi/syncHyperConfirm'
        logger.info('实时同步高血压确诊接口的url地址为：{}'.format(self.url))

    def hyper_confirm(self, session):
        # 入参
        data = {
            "personInfoId": None,
            "personInfoNo": None,
            "name": "糖尿病确诊2",
            "sexCode": "1",
            "drinking": "10",
            "age": "25",
            "sbp": "121",
            "dbp": "80",
            "bmi": "100",
            "waist": "55",
            "outerPersonId": "",
            "patientStatus": "3",
            "respDoctorId": "",
            "respDoctorName": "",
            "symptomCode": "",
            "symptomValue": "",
            "stapleFood": "",
            "isSmoking": "",
            "isDrinking": "",
            "dailySmoking": "",
            "exerciseDurationMins": "",
            "exerciseDurationTime": "",
            "birthday": "2007-03-07",
            "idNo": "11022919280101265X",
            "committee": "",
            "residenceTypeCode": "1",
            "nationalityCode": "01",
            "nationalityValue": "",
            "aboCode": "1",
            "educationCode": "1",
            "marriageCode": "1",
            "fixedPhones": "2323",
            "statusCode": "2",
            "deathDate": "",
            "systemSource": "1",
            "address": "东胜区建设街道办事处郝家圪卜村委会",
            "createOrgId": "60f5462b-2b4f-4cad-9645-83e1be0af87f",
            "orgName": "建设社区卫生服务中心",
            "creatorId": "939b2dcd-3851-43ac-bfb8-a421ad2d4306",
            "creator": "建设社区",
            "createTime": "2020-11-19 00:00:00",
            "modifiedOrgId": "60f5462b-2b4f-4cad-9645-83e1be0af87f",
            "modifiedOrgName": "建设社区卫生服务中心",
            "modifierId": "939b2dcd-3851-43ac-bfb8-a421ad2d4306",
            "modifier": "建设社区",
            "modifiedTime": "2020-11-19 15:15:00",
            "householdAddress": "东胜区建设街道办事处郝家圪卜村委会",
            "formerName": "",
            "workUnit": "",
            "contactName": "45454",
            "contactTelNo": "56565",
            "householdTypeCode": "",
            "rhCode": "3",
            "educationValue": "",
            "paperArchiveDate": "2020-11-18",
            "paperCardNum": "",
            "hyperConfirmedDate": "",
            "diabetesConfirmedDate": "",
            "familyDoctorId": "",
            "familyDoctorName": ""
        }
        HEADERS['access-token'] = setting.access_token
        logger.info('准备发起实时同步高血压确诊接口的请求，请求的header是：{},请求的参数是：{}'.format(HEADERS, data))
        # 发起请求
        response = session.post(self.url, json=data, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response


