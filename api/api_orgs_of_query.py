import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiOrgsOfQuery:
    '''
    查询当前用户机构下拉列表初始化数据接口
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<查询当前用户机构下拉列表初始化数据接口>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/org/initOrgOfQuery'
        logger.info('<查询当前用户机构下拉列表初始化数据接口>的url地址为：{}'.format(self.url))

    def orgs_of_query(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        logger.info('准备发起<查询当前用户机构下拉列表初始化数据接口>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.get(self.url, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        setting.organizationId = response.json()['result'][0].get('organizationId')  # 产生数据，并把数据放到setting当中
        logger.info('获取的响应值是：{}'.format(response))
        return response


if __name__ == '__main__':
    import requests

    print(ApiOrgsOfQuery().orgs_of_query(session=requests.session()))
    # print(ApiOrgsOfQuery().orgs_of_query(session=requests.session())['result'][0]['organizationId'])

