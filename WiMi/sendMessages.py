#coding=utf-8
from local_config import *
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# api.send_direct_message(user="@wimilive",text="test from python")
#

# with open('test.txt','r') as f:
#     nameList = f.readlines()
# print(type(nameList))
# print(nameList)
# print(nameList[0])

nameList = ['@patzuri_xxx','@wimilive','@iamKraTae ']

for name in nameList:
    api.send_direct_message(user=name, text="hello")