import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiDiabetesPatient:
    '''
    实时同步糖尿病高危、疑似接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取实时同步糖尿病高危、疑似接口的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/yfrhApi/syncDiabetesPatient'
        logger.info('实时同步糖尿病高危、疑似接口的url地址为：{}'.format(self.url))

    def diabetes_patient(self, session):
        # 入参
        data = {
            "personInfoId": "ff80808175b9fe730175baf0b54c0398",
            "personInfoNo": "15060200400700694",
            "name": "1112S1",
            "sexCode": "1",
            "drinking": "10",
            "age": "30",
            "sbp": "121",
            "dbp": "80",
            "bmi": "100",
            "waist": "55",
            "outerPersonId": "",
            "patientStatus": "1",
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
            "birthday": "1990-03-07",
            "idNo": "11022919280101011X",
            "committee": None,
            "residenceTypeCode": "1",
            "nationalityCode": "01",
            "nationalityValue": None,
            "aboCode": "1",
            "educationCode": "1",
            "marriageCode": "1",
            "fixedPhones": "2323",
            "hypertensionType": "1",
            "diabetesType": None,
            "statusCode": "2",
            "deathDate": None,
            "systemSource": None,
            "address": "东胜区建设街道办事处郝家圪卜社区郝家圪卜社区辖组",
            "createOrgId": "60f5462b-2b4f-4cad-9645-83e1be0af87f",
            "orgName": "建设社区卫生服务中心",
            "creatorId": "939b2dcd-3851-43ac-bfb8-a421ad2d4306",
            "creator": "建设社区",
            "createTime": "2020-11-26 00:00:00",
            "modifiedOrgId": "60f5462b-2b4f-4cad-9645-83e1be0af87f",
            "modifiedOrgName": "建设社区卫生服务中心",
            "modifierId": "939b2dcd-3851-43ac-bfb8-a421ad2d4306",
            "modifier": "建设社区",
            "modifiedTime": "2020-11-26 15:15:00",
            "householdAddress": "东胜区建设街道办事处郝家圪卜社区郝家圪卜社区辖组",
            "formerName": None,
            "workUnit": None,
            "contactName": "1212",
            "contactTelNo": "1212",
            "householdTypeCode": None,
            "rhCode": "3",
            "educationValue": None,
            "paperArchiveDate": "2020-11-26",
            "paperCardNum": None,
            "hyperConfirmedDate": None,
            "diabetesConfirmedDate": None,
            "familyDoctorId": None,
            "familyDoctorName": None
        }
        HEADERS['access-token'] = setting.access_token
        logger.info('准备发起实时同步糖尿病高危、疑似接口的请求，请求的header是：{},请求的参数是：{}'.format(HEADERS, data))
        # 发起请求
        response = session.post(self.url, json=data, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response
