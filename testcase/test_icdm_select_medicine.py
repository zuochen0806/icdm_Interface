import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_select_medicine import ApiSelectMedicine


@allure.feature('药品管理模块')
class TestSelectMedicine:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 实例化查询药品列表接口对象
        self.select_medicine_object = ApiSelectMedicine()

    @allure.story('用户正常登录后，查询药品列表')
    @allure.title('查询药品列表接口的测试用例')
    def test_select_medicine(self):
        '''
        测试是否能够查询药品列表
        前置：成功获取token
        '''
        # 发起请求
        response = self.select_medicine_object.select_medicine(self.session).json()
        # 断言
        assert response['message'] == '成功'
