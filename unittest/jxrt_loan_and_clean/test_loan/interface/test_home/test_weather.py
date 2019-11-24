import unittest
import requests
import json
from urllib import parse
from time import sleep

class weatherTest(unittest.TestCase):
    def setUp(self):

        self.url = 'http://t.weather.sojson.com/api/weather/city/'

    #正常流程
    def test_weather_tianjin(self):
        code = '101030100'
        r = requests.get(self.url+code)
        result = r.json()
        #  cityInfo
        self.assertEqual(result['status'],200)
        self.assertEqual(result['cityInfo']['city'],'天津市')
        sleep(3)

    #参数为空
    def test_weather_empty(self):
        #code = ''
        r = requests.get(self.url)
        result = r.json()
        #  cityInfo
        self.assertEqual(result['status'],404)
        self.assertEqual(result['message'],'Request resource not found.')
        sleep(3)

    #参数异常  r.json() 转换成字符串
    def test_weather_error(self):
        code = '天津'
        r = requests.get(self.url+code)
        result = r.json()
        #  cityInfo
        self.assertEqual(result['status'],404)
        self.assertEqual(result['message'],'Request resource not found.')
        sleep(3)
if __name__ == '__main__':
    unittest.main()