from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import requests
import json

#身份认证，BasicAuth 和 DigestAuth
base_url = 'http://httpbin.org'

# r = requests.get(base_url+'/basic-auth/51zxw/8888',auth = HTTPBasicAuth('51zxw','8888'))
# s = requests.get(base_url+'/basic-auth/51zxw/8888')
# print(r.text)
# print(r.status_code)
# #此时会报401，未授权
# print(s.status_code)
#
# d = requests.get(base_url+'/digest-auth/auth/zxw/6666',auth = HTTPDigestAuth('zxw','6666'))
# print(d.text)


#流式请求
stream = requests.get(base_url+'/stream/10',stream=True)
if stream.encoding is None:
    stream.encoding = 'UTF-8'

#对响应结果进行迭代处理
# json.loads:str转成dict      json.load是读取json数据
#json.dumps : dict转成str     json.dump是将python数据保存成json

#当下载大的文件的时候，建议使用strea模式．
# 默认情况下是false，他会立即开始下载文件并存放到内存当中，倘若文件过大就会导致内存不足的情况．
# 当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines
# 遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
# iter_content：一块一块的遍历要下载的内容
# iter_lines：一行一行的遍历要下载的内容

for line in stream.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(data['id'])

    print(data)

