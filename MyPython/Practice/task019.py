text = input('Enter a Text: ')
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)


from collections import Counter

freq = Counter(text)

print(dict(freq))
# Same output as above