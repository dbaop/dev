import requests
import json

class test_interface():
    def Interface(self,params,Interface_path):
        #封装请求参数
        pay={"userName":"admin","password":"123456"}
        r=requests.post('http://12.0.216.196:28080/xxl-job-admin/login',data=pay)#发起post登录接口请求
        headers =\
            {
            "Host": "12.0.216.196:28080",
            "Connection":"keep-alive",
           "Accept": "*/*",
           "Referer": "http://12.0.216.196:28080/xxl-job-admin/toLogin",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Origin": ": http://12.0.216.196:28080",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
           }  # 消息头

        print(r.headers)
        print(r.json())
        print(r.headers['Set-Cookie'])
        print(type(r.headers['Set-Cookie']))
        #通过登录接口获取token值给下个接口使用---
        head={
            "Cookie": str(r.headers['Set-Cookie']),
            # "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            #   "Host": "12.0.216.196:28080",
            #   "Origin": "http://12.0.216.196:28080",
            #   "Proxy-Connection": "keep-alive",
            #   "X-Requested-With": "XMLHttpRequest",
            #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
            #    (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            # "Connection": "keep - alive",
            # "Content - Length": "55",
            # "Accept": "application / json, text / javascript, * / *",
            # "X - Requested - With": "XMLHttpRequest",
            # "Referer": "http: // 12.0.216.196: 28080 / xxl - job - admin / jobinfo?jobGroup = 10",
            # "Accept - Encoding": "gzip, deflate",
            # "Accept - Language": "zh - CN, zh"
              }#将登录的head信息保存起来，让下个接口调用
        pay2=params#封装参数
        fimily=requests.post(Interface_path,params=pay2,headers=head)
        print(fimily)
        print(fimily.headers)
        print(fimily.text)
        # print(fimily.content)
    def Interface_biz(self, env, params, Interface_path):
        # 封装请求参数
        from urllib import parse
        user = {"mobile": "18601086706",
                # "bizPass": "ekviALdFBhcj00PvZJ01Mey9ewOUyqnvX7C8d4Rm4GhLwLI9DCupHGjZ8EavR4HmRY1U%2Ff2gzfndzmNsn6w4b4U5Ua"
                #            "FUgFmUkduDSu7vDMMotTaX2VX5o%2Fl9hfFrOOEWPkIiiPJgwa1BxuQ%2BS1FtwXx5O2F%2BnuqIzmOfchgZVp8%3D",
                "bizPass":"a1111111",
                # "_csrf" : "f8f2457d-baf2-4ecf-a644-29a387476343",
                "type":"CCBSCF_BUSINESS_WEB"
                }
        if env == 'T1':
            r_1 = requests.get('http://test1.ccbscf.com//uaa/token', data=json.dumps(user))
            session = r_1.json()
            print(session)
            print(r_1.content)
            da = r_1.json()['data']['token']
            print(r_1.json()['data']['token'])
            print(r_1.headers['Set-Cookie'])
            headers= {
                "Host": "test1.ccbscf.com",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "297",
                "Upgrade-Insecure-Requests": "1",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Referer": "http://test1.ccbscf.com/biz/login",
                "Origin": "http://test1.ccbscf.com",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                "Cookie": str(r_1.headers['Set-Cookie']),
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRF-Token":da

            }
            print(type(da))
            print(json.dumps(da).replace('r(\)',''))
            users = {"mobile": "13426064778",
                    "bizPass": "a1111111",
                    "type": "CCBSCF_BUSINESS_WEB"
                    }
            r = requests.post('http://test1.ccbscf.com/uaa/login',headers=headers)
            # 发起post登录接口请求
            headers = \
                {
                    "Host": "test1.ccbscf.com",
                    "Connection": "keep-alive",
                    "Cache-Control": "max-age=0",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Content-Length": "297",
                    "Upgrade-Insecure-Requests": "1",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "Referer": "http://test1.ccbscf.com/biz/login",
                    "Origin": "http://test1.ccbscf.com",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                    "Cookie": "root_domain_v=.ccbscf.com; _qddaz=QD.6clkfi.lwkvbb.jo6u007g; Hm_lvt_0c6e65449aadbf8373b13c\
                      5fe4f5ff56=1556189889,1557381631,1558494097,1558687430; sensorsdata2015jssdkcross=%7B%22distinct_id\
                      %22%3A%22cb2321d5-17e1-4119-89d1-d20b88cca497_6cb63950-e320-49a2-b682-43ed2aef6ae7%22%2C%22%24device_id\
                      %22%3A%2216add7ca2ba1a8-07e70e9e03e77c-353166-3686400-16add7ca2bb31f%22%2C%22props%22%3A%7B%22%\
                      24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type\
                      %22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%\
                      80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216add7ca2ba1a8-07e70e9e03e77c-353166-3686400-16add7ca2bb31f%22%7D",
                    "SESSION": "99043bea-df15-4f5e-92c5-3cd1c43ad650",
                    "X-CSRF-Token": da,
                    "_csrf": da
                }
            # 消息头
            print(r)
            print(r.content)
            print(r.text)
            # 通过登录接口获取token值给下个接口使用---
            head = {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRF-Token":da,
                "_csrf":da
            }
            #print(parse.urlencode(r_1))
            # 将登录的head信息保存起来，让下个接口调用
            pay2 = params  # 封装参数
            fimily = requests.get(Interface_path, params=pay2, headers=headers)
            print(fimily)

        if env == 'T2':
            r = requests.post('http://test2.ccbscf.com/uaa/login', data=user)  # 发起post登录接口请求
            headers = \
                {
                    "Host": "test2.ccbscf.com",
                    "Connection": "keep-alive",
                    "Cache-Control": "max-age=0",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "*/*",
                    "Referer": "http://test2.ccbscf.com/biz/login",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Origin": "http://test2.ccbscf.com",
                    "Accept-Encoding": "gzip, deflate",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                    "Cookie": "root_domain_v=.ccbscf.com; _qddaz=QD.6clkfi.lwkvbb.jo6u007g; Hm_lvt_0c6e65449aadbf8373b13c\
                      5fe4f5ff56=1556189889,1557381631,1558494097,1558687430; sensorsdata2015jssdkcross=%7B%22distinct_id\
                      %22%3A%22cb2321d5-17e1-4119-89d1-d20b88cca497_6cb63950-e320-49a2-b682-43ed2aef6ae7%22%2C%22%24device_id\
                      %22%3A%2216add7ca2ba1a8-07e70e9e03e77c-353166-3686400-16add7ca2bb31f%22%2C%22props%22%3A%7B%22%\
                      24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type\
                      %22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%\
                      80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216add7ca2ba1a8-07e70e9e03e77c-353166-3686400-16add7ca2bb31f%22%7D",
                    "SESSION": "99043bea-df15-4f5e-92c5-3cd1c43ad650"
                }
            # 通过登录接口获取token值给下个接口使用---
            head = {"Cookie": str(r.headers['Set-Cookie'])}
            # 将登录的head信息保存起来，让下个接口调用
            pay2 = params  # 封装参数
            fimily2 = requests.get(Interface_path, params=pay2, headers=head)
            print(fimily2)
        if env == 'T4':
            r = requests.post('http://test4.ccbscf.com/uaa/login', data=user)  # 发起post登录接口请求
            headers = \
                {
                    "Host": "test4.ccbscf.com",
                    "Connection": "keep-alive",
                    "Cache-Control": "max-age=0",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "*/*",
                    "Referer": "http://test4.ccbscf.com/biz/login",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Origin": "http://test4.ccbscf.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Cookie":"root_domain_v=.ccbscf.com; _qddaz=QD.6clkfi.lwkvbb.jo6u007g; Hm_lvt_0c6e65449aadbf8373b13c\
                             5fe4f5ff56=1556189889,1557381631,1558494097,1558687430; sensorsdata2015jssdkcross=%7B%22distinct_id\
                             %22%3A%22cb2321d5-17e1-4119-89d1-d20b88cca497_6cb63950-e320-49a2-b682-43ed2aef6ae7%22%2C%22%24device_id\
                             %22%3A%2216add7ca2ba1a8-07e70e9e03e77c-353166-3686400-16add7ca2bb31f%22%2C%22props%22%3A%7B%22%\
                             24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type\
                             %22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%\
                             80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216add7ca2ba1a8-07e70e9e03e77c-353166-3686400-16add7ca2bb31f%22%7D",
                   "SESSION":"99043bea-df15-4f5e-92c5-3cd1c43ad650",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
                }
            # 通过登录接口获取token值给下个接口使用---
            head = {"Cookie": str(r.headers['Set-Cookie'])}
            # 将登录的head信息保存起来，让下个接口调用
            pay2 = params  # 封装参数
            fimily4 = requests.get(Interface_path, params=pay2, headers=head)
            print(fimily4)