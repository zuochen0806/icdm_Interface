import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_pos_sessions import ApiPosSessions
from api.api_overall_statistics import ApiOverallStatistics


@allure.feature('济南慢病大屏模块')
class TestOverallStatistics:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用获取当前登录用户信息接口
        ApiPosSessions().pos_session(self.session)
        # 实例化查询慢病患者总体统计接口（地图）对象
        self.overall_statistics_object = ApiOverallStatistics()

    @allure.story('用户正常登录后，查询慢病患者总体统计（地图）')
    @allure.title('查询慢病患者总体统计接口（地图）的测试用例')
    def test_overall_statistics(self):
        '''
        测试是否能够查询慢病患者总体统计（地图）
        前置：成功获取token
        '''
        # 发起请求
        response = self.overall_statistics_object.overall_statistics(self.session).json()
        # 断言
        assert response['message'] == '成功'
