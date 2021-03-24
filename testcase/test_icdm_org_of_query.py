import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_orgs_of_query import ApiOrgsOfQuery
from api.api_org_of_query import ApiOrgOfQuery


@allure.feature('字典相关模块')
class TestOrgOfQuery:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用查询当前用户机构下拉列表初始化数据接口
        ApiOrgsOfQuery().orgs_of_query(self.session)
        # 实例化根据机构Id查询子级机构信息接口对象
        self.org_of_query_object = ApiOrgOfQuery()

    @allure.story('用户正常登录后，根据机构Id查询子级机构信息')
    @allure.title('根据机构Id查询子级机构信息的测试用例')
    def test_org_of_query(self):
        '''
        测试是否能够根据机构Id查询子级机构信息
        前置：成功获取token
        '''
        # 发起请求
        response = self.org_of_query_object.org_of_query(self.session).json()
        # 断言
        assert response['message'] == '成功'
