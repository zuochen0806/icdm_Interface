import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_diabetes_patient import ApiDiabetesPatient


@allure.feature('第三方实时同步模块')
class TestDiabetesPatient:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化实时同步糖尿病高危、疑似接口对象
        self.diabetes_patient_object = ApiDiabetesPatient()

    @allure.story('用户正常登录后，第三方实时同步糖尿病高危、疑似接口')
    @allure.title('实时同步糖尿病高危、疑似接口的测试用例')
    def test_diabetes_patient(self):
        '''
        测试第三方接口是否能够实时同步糖尿病高危、疑似患者
        前置：成功获取token
        '''
        # 发起请求
        response = self.diabetes_patient_object.diabetes_patient(self.session).json()
        # 断言
        assert response['message'] == '成功'
