import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_pos_sessions import ApiPosSessions
from api.api_manage_oderby_district import ApiManageOderbyDistrict


@allure.feature('济南慢病大屏模块')
class TestManageOderbyDistrict:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用获取当前登录用户信息接口
        ApiPosSessions().pos_session(self.session)
        # 实例化查询各地区慢病患者管理排名接口对象
        self.manage_oderby_district_object = ApiManageOderbyDistrict()

    @allure.story('用户正常登录后，查询各地区慢病患者管理排名')
    @allure.title('查询各地区慢病患者管理排名接口的测试用例')
    def test_manage_oderby_district(self):
        '''
        测试是否能够查询各地区慢病患者管理排名
        前置：成功获取token
        '''
        # 发起请求
        response = self.manage_oderby_district_object.manage_oderby_district(self.session).json()
        # 断言
        assert response['message'] == '成功'
