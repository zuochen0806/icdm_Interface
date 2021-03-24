# 获取jenkins构建信息和本次报告地址
import jenkins  # 安装pip install python-jenkins
import json
import urllib3

from setting import DIR_NAME

# jenkins登录地址
jenkins_url = "http://192.168.1.62:8080/jenkins"
# 获取jenkins对象
server = jenkins.Jenkins(jenkins_url, username='admin', password='123456')  # Jenkins登录名 ，密码
# job名称
job_name = "/job/icdm_Interface/"  # Jenkins运行任务名称
# job的url地址
job_url = jenkins_url + job_name
# 获取最后一次构建
job_last_build_url = server.get_info(job_name)['lastBuild']['url']
# 报告地址
report_url = job_last_build_url + 'allure/'

'''
钉钉推送方法：
读取report文件中"prometheusData.txt"，循环遍历获取需要的值。
使用钉钉机器人的接口，拼接后推送text
'''


def DingTalkSend():
    d = {}
    # 打开prometheusData 获取需要发送的信息
    f = open(DIR_NAME + r'/allure-report/export/prometheusData.txt', 'r')
    # f = open(DIR_NAME + r'/reports/html/export/prometheusData.txt', 'r')
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    print(d)
    f.close()
    retries_run = d.get('launch_retries_run')  # 运行总数
    print('运行总数: {}个'.format(retries_run))
    status_passed = d.get('launch_status_passed')  # 通过数量
    print('通过数量：{}个'.format(status_passed))
    status_failed = d.get('launch_status_failed')  # 失败数量
    print('失败数量：{}个'.format(status_failed))
    status_broken = d.get('launch_status_broken')  # 故障数量
    print('故障数量：{}个'.format(status_broken))
    status_skipped = d.get('launch_status_skipped')  # 跳过数量
    print('跳过数量：{}个'.format(status_skipped))
    status_unknown = d.get('launch_status_unknown')  # 未知数量
    print('未知数量：{}个'.format(status_unknown))
    retries_retries = d.get('launch_retries_retries')  # 重试数量
    print('重试数量：{}个'.format(retries_retries))
    time_duration = d.get('launch_time_duration')  # 总用时
    print('总用时：{}ms'.format(time_duration))
    time_min_duration = d.get('launch_time_min_duration')  # 单个接口最少用时
    print('单个接口最少用时：{}ms'.format(time_min_duration))
    time_max_duration = d.get('launch_time_max_duration')  # 单个接口最多用时
    print('单个接口最多用时：{}ms'.format(time_max_duration))
    time_sum_duration = d.get('launch_time_sum_duration')  # 所有接口总用时
    print('所有接口总用时：{}ms'.format(time_sum_duration))

    # 钉钉推送
    url = 'https://oapi.dingtalk.com/robot/send?access_token=b28eb95f77157f23364f5763d5af9117ac9d8c591374b74b705fe40a7632aa9c'  # webhook
    con = {"msgtype": "text",
           "text": {
               "content": "<<本消息是程序⾃动下发的，请勿回复！>>\n"
                          "{}执行完成。".format(server.get_info(job_name)['description']) +
                          "\n测试概述："
                          "\n项目名称：{}".format(server.get_info(job_name)['name']) +
                          "\n运行总数：{} 个".format(retries_run) +
                          "\n通过数量：{} 个".format(status_passed) +
                          "\n失败数量：{} 个".format(status_failed) +
                          "\n故障数量：{} 个".format(status_broken) +
                          "\n重试数量：{} 个".format(status_skipped) +
                          "\n未知数量：{} 个".format(status_unknown) +
                          "\n重试数量：{} 个".format(retries_retries) +
                          "\n总用时：{} ms".format(time_duration) +
                          "\n单个接口最少用时：{} ms".format(time_min_duration) +
                          "\n单个接口最多用时：{} ms".format(time_max_duration) +
                          "\n所有接口总用时：{} ms".format(time_sum_duration) +
                          "\n构建地址：\n{}".format(job_url) +
                          "\n报告地址：\n{}".format(report_url)
           }
           }
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    jd = json.dumps(con)
    jd = bytes(jd, 'utf-8')
    http.request('POST', url, body=jd, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    DingTalkSend()
