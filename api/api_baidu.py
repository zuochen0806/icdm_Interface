import requests
import warnings

warnings.filterwarnings('ignore')
# r = requests.get('https://www.baidu.com/', verify=False)
r = requests.get('http://127.0.0.1:5000/login', verify=False)
print(r.json())
