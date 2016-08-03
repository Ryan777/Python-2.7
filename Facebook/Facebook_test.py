#coding=utf-8
# https://graph.facebook.com/{user_id}?access_token=EAACclRwpTsYBAD2BPDQcwiEUMy0RrG82DQYmEYjge7qiWftZBi44WhJGUp7txULbUmoCD58PBkZA3OUZAujgYbWJkHqpie56ZBLjW5dOQcff8yfZCPS2xboJrK70pZBkFYqUz4YkjzKioBdPv2gleUknEKFrXZBTAxEZCTXfLRZAQXkfAkwmwRDAW
import requests
import json
import facebook


token = 'EAACEdEose0cBAMKhGnWcXDmO62LSQqUjLwSPb7560DQAoLaLtU9zSPDjeHdfnjn2GXBppAeEK7BIbiVgARcBhLpAG6eZCzO16Lss0gwJxn50M3ZC3xAuTZA45m0mCm9xFIiFEbdVIHzVuZA7QAY4HracOlrfZCqcfZArP1YxFWDLwpGYymZCFl0xa8tfys0U4ODuCZBtwB6WWzMdM6f9Xnz4'
# res = requests.get('https://graph.facebook.com/v2.7/724335199?access_token=%s'%(token))

# res = requests.get('https://graph.facebook.com/v2.7/me?access_token=%s'%(token))
# print res.text
# result = json.loads(res.text)

# print result['id']

# key = 'access_token=EAACEdEose0cBACdFfwpLmaMiDYN1bYM6Pjcdf3oBsfOv4IoOHhHcfjZBK8vFj7gqKyI1hUMZCnmPYmTdX67Vff294O3WTZCkdxc1rbdjvzXvspt6HpIqtSEyukymvdUgZBaZBGe77YtfscrLB9ZBPxTztvLhjzgz4Q4vjBgzPtJIPVQSp9p81d'
res = requests.post('http://graph.facebook.com/me/feed?message="Hello, World.')
#
# api = facebook.GraphAPI(token)
# msg = "Hello world from Python"
# status = api.put_wall_post(msg)

graph_url = ( "https://graph.facebook.com/me/feed?" +
"access_token=" + token )
