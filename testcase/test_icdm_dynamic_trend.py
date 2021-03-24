import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_pos_sessions import ApiPosSessions
from api.api_dynamic_trend import ApiDynamicTrend


@allure.feature('济南慢病大屏模块')
class TestDynamicTrend:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用获取当前登录用户信息接口
        ApiPosSessions().pos_session(self.session)
        # 实例化查询患者动态趋势分布接口对象
        self.dynamic_trend_object = ApiDynamicTrend()

    @allure.story('用户正常登录后，查询患者动态趋势分布')
    @allure.title('查询患者动态趋势分布接口的测试用例')
    def test_overall_statistics(self):
        '''
        测试是否能够查询患者动态趋势分布
        前置：成功获取token
        '''
        # 发起请求
        response = self.dynamic_trend_object.dynamic_trend(self.session).json()
        # 断言
        assert response['message'] == '成功'
