# url = http://t.weather.sojson.com/api/weather/city/101030100    最后那个是city_code
# 查json  http://www.bejson.com/
# HTMLTestRunner下载地址  https://github.com/easonhan007/HTMLTestRunner
# 天气  https://www.tianqiapi.com/api/?city=北京
#导入json 做编码用，把中文字符转换  get 是 params , post 是 date
import requests
from urllib import parse
import json

# data = {'city':'北京'}
# city = parse.urlencode(data).encode('UTF-8')
# #city = parse.urlencode(data).encode('GBK')
# url = 'https://www.tianqiapi.com/api/'
# r = requests.get(url,params=city)
# print(r.text)
# repose = r.json()
# #print(repose['data'])
# print(repose['city'])data = {'city':'北京'}
# # city = parse.urlencode(data).encode('UTF-8')
# # #city = parse.urlencode(data).encode('GBK')
# # url = 'https://www.tianqiapi.com/api/'
# # r = requests.get(url,params=city)
# # print(r.text)
# # repose = r.json()
# # #print(repose['data'])
# # print(repose['city'])


#data1 = {'code':'101030100'}
code = '101030100'
url1 = 'http://t.weather.sojson.com/api/weather/city/%s'%code
r1 = requests.get(url1)
print(r1.text)
repose = r1.json()
print(repose['date'])
print(repose['status'])
print(repose['cityInfo']['city'])
#取数组
print(repose['data']['forecast'][0]['week'])