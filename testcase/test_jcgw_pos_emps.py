import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_pos_emps import ApiPosEmps
from api.api_pos_sessions import ApiPosSessions


@allure.feature('登录模块')
class TestPosEmps:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用获取当前登录用户信息接口
        ApiPosSessions().pos_session(self.session)
        # 实例化获取医卫人员信息接口对象
        self.pos_emps_object = ApiPosEmps()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('用户正常登录后，获取医卫人员信息')
    @allure.title('获取医卫人员信息接口的测试用例')
    def test_pos_emps(self):
        '''
        测试是否能够获取医卫人员信息信息
        前置：成功获取token
        '''
        # 发起请求
        response = self.pos_emps_object.pos_emps(self.session).json()
        # 断言
        assert response[0]['emp_name'] == '白鹤'
