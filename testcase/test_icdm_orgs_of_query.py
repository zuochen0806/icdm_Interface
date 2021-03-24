import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_orgs_of_query import ApiOrgsOfQuery


@allure.feature('字典相关模块')
class TestOrgsOfQuery:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化查询当前用户机构下拉列表初始化数据接口对象
        self.orgs_of_query_object = ApiOrgsOfQuery()

    @allure.story('用户正常登录后，获取当前用户机构下拉列表初始化数据')
    @allure.title('查询当前用户机构下拉列表初始化数据接口的测试用例')
    def test_orgs_of_query(self):
        '''
        测试是否能够获取当前用户机构下拉列表初始化数据
        前置：成功获取token
        '''
        # 发起请求
        response = self.orgs_of_query_object.orgs_of_query(self.session).json()
        # 断言
        assert response['message'] == '成功'
