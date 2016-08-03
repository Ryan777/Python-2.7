#coding=utf-8
import urllib
import requests
from bs4 import BeautifulSoup
import time

for i in range(71,75):
    original_link = 'http://www.houseoflover.com/hol/home/friendfind.aspx?usex=M&sex=M&age1=18&age2=50&livein=all&page='+str(i)
    response = requests.get(original_link)
    soup = BeautifulSoup(response.text,'html.parser')
    links = soup.findAll("",{'class':'FrdPic150'})
    for link in links:
        link_level2_raw = link.a['href']
        link_level2 = link_level2_raw.replace('../..','http://www.houseoflover.com/')
        response_level2 = requests.get(link_level2)
        soup_level2 = BeautifulSoup(response_level2.text, 'html.parser')
        result = soup_level2.findAll(attrs = {'class':"MaxContentPic"})
        for link in result:
            ## find the entire tag, then link['src'] points to the 'src' attr within this tag.
            link_raw = link['src']
            link = link_raw.replace('../..','http://www.houseoflover.com/')
            print link
            fileName = time.strftime("%Y%m%d%H%M%S", time.localtime(int(time.time())))+'.jpeg'
            urllib.urlretrieve(link,fileName)
