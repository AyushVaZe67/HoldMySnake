import re


pattern = r'[a-z]nd'
text = ('The sun dipped below the horizon, casting a warm orange glow across the quiet countryside. land sand stand '
        'Birds chirped their final songs of the day as a gentle breeze rustled the leaves of tall trees lining the dirt path. '
        'In the distance, a small cottage with smoke rising from its chimney promised comfort and warmth. '
        'Everything felt peaceful, as if time had slowed down just for a moment.')


# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)
print(matches)
for i in matches:
    print(i)

