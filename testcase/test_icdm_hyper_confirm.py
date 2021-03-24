import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_hyper_confirm import ApiHyperConfirm


@allure.feature('第三方实时同步模块')
class TestHyperConfirm:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化实时同步高血压确诊接口对象
        self.hyper_confirm_object = ApiHyperConfirm()

    @allure.story('用户正常登录后，第三方实时同步高血压确诊接口')
    @allure.title('实时同步高血压确诊接口的测试用例')
    def test_hyper_confirm(self):
        '''
        测试第三方接口是否能够实时同步高血压确诊患者
        前置：成功获取token
        '''
        # 发起请求
        response = self.hyper_confirm_object.hyper_confirm(self.session).json()
        # 断言
        assert response['message'] == '成功'
