# # f = open('myfile.txt','r')
# # f1 = open('myfile1.txt','w')
# f2 = open('myfile1.txt','a')
# text = 'New text'
# # f.write(text)
#
# f2.write('Appended Text')
#
# # f.close()
# # f1.close()
# f2.close()

with open('myfile.txt') as f:
    print(f.read())
