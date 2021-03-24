import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_role_menu import ApiRoleMenu


@allure.feature('字典相关模块')
class TestRoleMenu:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化查询当前用户菜单字典接口对象
        self.role_menu_object = ApiRoleMenu()

    @allure.story('用户正常登录后，查询当前用户菜单字典')
    @allure.title('查询当前用户菜单字典接口的测试用例')
    def test_role_menu(self):
        '''
        测试是否能够查询当前用户菜单字典
        前置：成功获取token
        '''
        # 发起请求
        response = self.role_menu_object.role_menu(self.session).json()
        # 断言
        assert response['message'] == '成功'
