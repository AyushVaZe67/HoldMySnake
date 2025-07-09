text = input('Enter a String: ')
text1 = text.lower()

list1 = []
for i in range(len(text1)):
    list1.append(text1[i])

# print(list1)


list2 = []
for i in range(1,len(text1)+1):
    list2.append(text1[-i])

# print(list2)


if list1 == list2:
    print('Given string is palindrome')
else:
    print('Given string is not palindrome')