#coding=utf-8
#coding=utf-8
import requests
import json
from bs4 import BeautifulSoup

#success
#https://graph.facebook.com/me?access_token=EAACEdEose0cBAPFcXyF1ZBeLBUZAoPuTJz6VD9XYgp1Aafu8zKu7rA4X5deakNLVZAQ6acgSCNpH2RZBDLiaM9Ra0ibsLgDtAoDBHIMJ3lrMgzNbALPpPlkQwbKZA7kSacteZBnrAs4LR1sCN86UDM8pdZAXrG2e6mUmoSPLZAnw2wZDZD

key = 'access_token=EAACEdEose0cBAPFcXyF1ZBeLBUZAoPuTJz6VD9XYgp1Aafu8zKu7rA4X5deakNLVZAQ6acgSCNpH2RZBDLiaM9Ra0ibsLgDtAoDBHIMJ3lrMgzNbALPpPlkQwbKZA7kSacteZBnrAs4LR1sCN86UDM8pdZAXrG2e6mUmoSPLZAnw2wZDZD'
url = 'https://graph.facebook.com/me/photos?'

request = requests.get(url+key)
all_data = json.loads(request.text)

print all_data