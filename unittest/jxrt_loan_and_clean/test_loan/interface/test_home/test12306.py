#r = requests.get("https://www.12306.cn")
#r = requests.get("https://www.12306.cn",verify = False)
# print(r.text)



#代理设置  www.xicidaili.com

import requests
import json
proxies = { "http": "http://111.231.94.44:8888", "https": "https://111.231.92.21:8888", }
r = requests.get("https://www.12306.cn", proxies=proxies)
# s = json.dumps(r)
w = requests.get("http://www.baidu.com", proxies=proxies)

# print(r.text)
#print(w.text)
#print(w.json())
print(r.headers)
#print(r.json())
