#coding=utf-8
import urllib
import urllib2
import re
import requests
from cStringIO import StringIO
# from PIL import Image
from bs4 import BeautifulSoup


url = 'http://www.houseoflover.com/hol/home/meminfo.aspx?memid=Rinn'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print soup.prettify()

# # links = soup.findAll(attrs = {'class':'page_name'})
# print soup.a
# soup.select('a[href^=/twitter/detail]')
result = soup.findAll(attrs = {'class':"MaxContentPic"})
name = 1
for link in result:
    link_raw = link['src']
    link = link_raw.replace('../..','http://www.houseoflover.com/')
    print link
    urllib.urlretrieve(link,str(name)+'.jpeg')
    name+=1
# print soup.img['src']