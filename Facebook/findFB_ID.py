#coding=utf-8
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re


# html = requests.get('https://m.facebook.com/')
#
# bsObj = BeautifulSoup(html.text,'html.parser')
# print bsObj.prettify()

data = {
    'lsd': 'AVq12Zz9',
    'charset_test': "€,´,€,´,水,Д,Є",
    'version': '1',
    'ajax': '0',
    'width': '0',
    'pxr': '0',
    'gps': '0',
    'm_ts': "1470045306",
    'li': 'ehyfV4hMHU2gaGfe2fYybpyL',
}
data['email'] = '116501169@qq.com'
data['pass'] = 'rrr380654'
data['login'] = 'Log In'

url = 'https://m.facebook.com/'
s = requests.Session()
r = s.post(url, data=data)
r.raise_for_status()

page = requests.get('https://www.facebook.com/StudentCuteGirlsTh/')
soup = BeautifulSoup(page.text, 'html.parser')

print soup.prettify()