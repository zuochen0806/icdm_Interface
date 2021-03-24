import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_pos_sessions import ApiPosSessions


@allure.feature('登录模块')
class TestPosSessions:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化获取当前登录用户信息接口对象
        self.pos_sessions_object = ApiPosSessions()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('用户正常登录后，获取用户信息')
    @allure.title('获取当前登录用户信息接口的测试用例')
    def test_pos_sessions(self):
        '''
        测试是否能够获取当前用户信息
        前置：成功获取token
        '''
        # 发起请求
        response = self.pos_sessions_object.pos_session(self.session).json()
        # 断言
        assert response['account_username'] == 'xiang01'
