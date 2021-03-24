import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiOrgOfQuery:
    '''
    根据机构Id查询子级机构信息
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<根据机构Id查询子级机构信息>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/org/initOrgOfQuery'
        logger.info('<根据机构Id查询子级机构信息>的url地址为：{}'.format(self.url))

    def org_of_query(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        data = {'organizationId': setting.organizationId}  # 调用配置文件中的access_token
        logger.info('准备发起<根据机构Id查询子级机构信息>的请求，请求的header是：{},请求的参数是：{}'.format(HEADERS, data))
        # 发起请求
        response = session.get(self.url, params=data, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response


if __name__ == '__main__':
    import requests

    print(ApiOrgOfQuery().org_of_query(session=requests.session()).json())
