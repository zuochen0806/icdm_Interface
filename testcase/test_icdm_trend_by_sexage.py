import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_pos_sessions import ApiPosSessions
from api.api_trend_by_sexage import ApiTrendBySexage


@allure.feature('济南慢病大屏模块')
class TestTrendBySexage:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用获取当前登录用户信息接口
        ApiPosSessions().pos_session(self.session)
        # 实例化查询患者年龄性别分布接口对象
        self.trend_by_sexage_object = ApiTrendBySexage()

    @allure.story('用户正常登录后，查询患者年龄性别分布')
    @allure.title('查询患者年龄性别分布接口的测试用例')
    def test_trend_by_sexage(self):
        '''
        测试是否能够查询患者年龄性别分布
        前置：成功获取token
        '''
        # 发起请求
        response = self.trend_by_sexage_object.trend_by_sexage(self.session).json()
        # 断言
        assert response['message'] == '成功'
