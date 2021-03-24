import setting
from setting import JCGW_IP, PORT3, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()


class ApiDeleteTreatPlanByid:
    '''
    删除治疗方案接口（支持批量）
    '''

    def __init__(self):
        '''
        todo 初始化
        '''
        logger.info('开始获取<删除治疗方案接口（支持批量）>的url地址：')
        # 构造url地址
        self.url = JCGW_IP + ':' + PORT3 + '/icdm-controller/treatPlan/deleteTreatPlanById/'
        logger.info('<删除治疗方案接口（支持批量）>的url地址为：{}'.format(self.url))

    def delete_treat_plan_byid(self, session):
        # 入参
        HEADERS['access-token'] = setting.access_token
        data = [setting.datas[0]]
        logger.info('准备发起<删除治疗方案接口（支持批量）>的请求，请求的header是：{}'.format(HEADERS))
        # 发起请求
        response = session.post(self.url, json=data, headers=HEADERS)
        logger.info('请求的url是：{}'.format(response.url))
        logger.info('获取的响应值是：{}'.format(response))
        return response


if __name__ == '__main__':
    import requests

    ApiDeleteTreatPlanByid().delete_treat_plan_byid(session=requests.session())
