import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_select_treat_planlist import ApiSelectTreatPlanlist
from api.api_select_use_medicine_byid import ApiSelectUseMedicineById


@allure.feature('治疗方案模块')
class TestSelectUseMedicineById:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用查询治疗方案列表接口
        ApiSelectTreatPlanlist().select_treat_planlist(self.session)
        # 实例化根据治疗方案id查询治疗方案详情接口对象
        self.select_use_medicine_byid_object = ApiSelectUseMedicineById()

    @allure.story('用户正常登录后，根据治疗方案id查询治疗方案详情')
    @allure.title('根据治疗方案id查询治疗方案详情接口的测试用例')
    def test_select_use_medicine_byid(self):
        '''
        测试是否能够根据治疗方案id查询治疗方案详情
        前置：成功获取token
        '''
        # 发起请求
        response = self.select_use_medicine_byid_object.select_use_medicine_byid(self.session).json()
        # 断言
        assert response['message'] == '成功'
