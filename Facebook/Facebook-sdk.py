#coding=utf-8
import facebook

graph = facebook.GraphAPI('EAACEdEose0cBAILt19cK6nn22kHren4ezAdFSxdNkD7P3sBpvbhxkiFVpmRZCkmtYrSXCnGOtZAZBghvHOTK6z234yd5Dz6YABFNBYiDD8Khkc97B6iHMTJzilcZCrZBF59t6Tx6F19ZCQ7D3JwZAWJdihnCeaR1Q0xtZCNeRbl1ifxFMZB3gwfB4', version = 2.5)

myProfile = graph.get_object('me')
# graph.put_object('me','feed',message = "Test via SDK")
email = myProfile['id']
print email