
with open('test.txt','r') as f:
    nameList = f.readlines()
print(type(nameList))
print(nameList)
print(nameList[0])