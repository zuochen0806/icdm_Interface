import allure
import requests

from api.api_get_token import ApiGetToken
from api.api_select_treat_planlist import ApiSelectTreatPlanlist
from api.api_update_treat_plan_byid import ApiUpdateTreatPlanById


@allure.feature('治疗方案模块')
class TestUpdateTreatPlanById:
    # 在所有的测试用例之前创建session
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功获取token接口
        ApiGetToken().get_token_success(self.session)
        # 调用查询治疗方案列表接口
        ApiSelectTreatPlanlist().select_treat_planlist(self.session)
        # 实例化新增/编辑治疗方案接口对象
        self.update_treat_plan_byid_object = ApiUpdateTreatPlanById()

    @allure.story('用户正常登录后，新增/编辑治疗方案')
    @allure.title('新增/编辑治疗方案接口的测试用例')
    def test_update_treat_plan_byid(self):
        '''
        测试是否能够新增/编辑治疗方案接口
        前置：成功获取token
        '''
        # 发起请求
        response = self.update_treat_plan_byid_object.update_treat_plan_byid(self.session).json()
        # 断言
        assert response['message'] == '成功'
