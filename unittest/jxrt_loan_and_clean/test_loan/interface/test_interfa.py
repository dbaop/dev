import requests


r=requests.post(
    url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
    data={'cityId':438})
print (r.json())