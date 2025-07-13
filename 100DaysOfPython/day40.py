import random
import string
msg1 = input('Enter a message to encode: ')
random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))
random_letters1 = ''.join(random.choices(string.ascii_lowercase, k=3))

if len(msg1) < 4:
    encoded = msg1[::-1]
else:
    last_letter = msg1[-1]
    msg1 = msg1[:-1]
    encoded1 = last_letter + msg1
    encoded = random_letters + encoded1 + random_letters1

print(encoded)
