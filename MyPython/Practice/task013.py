text = input('Enter a text: ')
text1 = text.lower()

vowel,consonant = 0,0
for i in range(len(text1)):
    if text1[i] == 'a' or text1[i] == 'u' or text1[i] == 'o' or text1[i] == 'i' or text1[i] == 'e':
        vowel += 1
    else:
        consonant += 1


print('Vowels:', vowel)
print('Consonants:',consonant)