file = open('file.txt','r')

content = file.read()
content1 = file.readlines()

print(content)
print(content1)

file.close()
