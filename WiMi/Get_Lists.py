#coding=utf-8
# view-source:http://zocialrank.com/inner_twitter.php?cc=TH&page=1
import requests
from bs4 import BeautifulSoup

response = requests.get('http://zocialrank.com/inner_twitter.php?cc=TH')
soup = BeautifulSoup(response.text,"html.parser")

# names = [a.attrs.get('href') for a in soup.select('a[href^=/twitter/detail]')]
# print soup.prettify()

names = soup.findAll(attrs = {'class':'page_name'})

with open('test.txt','a') as f:

    for name in names:
        f.write(name.text)
        f.write('\n')
        print(name.text)

# # Read list as a List object
# with open('test.txt','r') as f:
#     nameList = f.readlines()
# print(type(nameList))
# print(nameList)
# print(nameList[0])