import allure
import pytest
import requests

from api.api_get_token import ApiGetToken
from setting import DIR_NAME
from tools.readData import ReadData

# 读取测试数据
data_li = ReadData().get_yaml('get_token_data', 'test_get_token')


@allure.feature('登录模块')
# @allure.link(url='', name='link_url：{}'.format(ApiGetToken().url))
# @allure.description('测试获取token功能，用户使用不同的账号成功登录后均可正常获取正确的token')
class TestGetToken:
    def setup_class(self):
        '''
        在所有的测试用例之前创建session
        '''
        # 获取session对象
        self.session = requests.session()
        # 实例化获取token接口对象
        self.gettoken_object = ApiGetToken()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('用户密码正确，成功获取token')
    @allure.title('获取token接口的测试用例')
    # @allure.testcase('http:''www.baicu.com')
    # @allure.step('测试成功获取token')
    @pytest.mark.parametrize('dic', data_li)
    def test_get_token(self, dic):
        '''
        测试获取token功能，用户使用不同的账号成功登录后均可正常获取正确的token
        '''
        # 读取数据，进行构造data,然后发起请求
        data = {'username': dic['username'], 'password': dic['password']}
        with allure.step('1.输入用户名：{} 2.输入密码：{} 3.点击登录按钮'.format(dic['username'], dic['password'])):
            response = self.gettoken_object.get_token(self.session, data).json()
        with open(DIR_NAME + '/data/login_page.png', mode='rb') as f:
            file = f.read()
            allure.attach(file, '登录页面', allure.attachment_type.PNG)
        # 断言
        assert response['username'] == dic['username']


if __name__ == '__main__':
    print(ApiGetToken().url)
