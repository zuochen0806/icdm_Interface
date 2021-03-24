import yaml

from setting import DIR_NAME


class ReadData:
    def get_yaml(self, filename, key):
        '''
        解析yaml，yml文件，得到列表嵌套字典的数据格式
        '''
        with open(DIR_NAME + '/data/%s.yml' % filename, encoding='utf-8') as f:
            # 最新的知识点
            yaml_data = yaml.safe_load(f)
            # print(yaml_data)
            # 构造空的列表
            # data_list = []
            cases_dict = yaml_data.get(key)
            # case_object是可迭代对象  for ...in..,list(),列表.extend()
            case_object = cases_dict.values()
            # print(case_object)
            # data_list.extend(case_object)
            data = list(case_object)
            return data


if __name__ == '__main__':
    # all_cases=ReadExcel().get_excel()
    # print(all_cases)
    print(ReadData().get_yaml('login_data', 'test_login'))
