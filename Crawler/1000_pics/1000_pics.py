#coding=utf-8
import urllib
import urllib2
import re
import requests
from cStringIO import StringIO
# from PIL import Image
from bs4 import BeautifulSoup

### Login function
login_url = 'http://www.jubkoo.com/signin.php'
payload = {'username':'dog1123','password':'123456','remember_signin':'true'}
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0'}
s = requests.Session()
r = s.post(login_url,data=payload,headers= header)
soup = BeautifulSoup(r.text,'html.parser')
print soup
### Made sure it is successful


# html = requests.get('http://www.jubkoo.com/search/show_main_pic.php?mem_id=267254&pic_id=768789')
# soup = BeautifulSoup(html.text,"html.parser")
# print soup

# def saveImg(self,imageURL,fileName):
#     u = urllib.urlopen(imageURL)
#     data = u.read()
#     f = open(fileName, 'wb')
#     f.write(data)
#     f.close()
#
#
# saveImg('http://www.jubkoo.com/search/show_main_pic.php?mem_id=267254&pic_id=768789','test')
#
# def downloadImageFile(imgUrl):
#     local_filename = '123.jpeg'
#     print "Download Image File=", local_filename
#     r = requests.get(imgUrl, stream=True) # here we need to set stream = True parameter
#     with open(local_filename, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk: # filter out keep-alive new chunks
#                 f.write(chunk)
#                 f.flush()
#         f.close()
#     return local_filename
# downloadImageFile('http://www.jubkoo.com/search/show_main_pic.php?mem_id=267254&pic_id=768789')

url = 'http://www.houseoflover.com/friend/more/P/popchish111IV44C1E51Z0FZGN30625562656.jpg'
urllib.urlretrieve(url, 'ำ้ำเฟหไดพเพ้ร.jpeg')
