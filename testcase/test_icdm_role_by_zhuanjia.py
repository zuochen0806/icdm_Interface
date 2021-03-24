import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_role_by_zhuanjia import ApiRoleByZhuanjia


@allure.feature('字典相关模块')
class TestRoleByZhuanjia:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化查询所有专家角色信息接口对象
        self.role_by_zhuanjia_object = ApiRoleByZhuanjia()

    @allure.story('用户正常登录后，查询所有专家角色信息')
    @allure.title('查询所有专家角色信息接口的测试用例')
    def test_role_by_zhuanjia(self):
        '''
        测试是否能够查询所有专家角色信息
        前置：成功获取token
        '''
        # 发起请求
        response = self.role_by_zhuanjia_object.role_by_zhuanjia(self.session).json()
        # 断言
        assert response['message'] == '成功'
