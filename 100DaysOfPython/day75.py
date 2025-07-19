import os

# os.rename('myfile1.txt','myfile4.txt')

files = os.listdir('images')

i = 1
for file in files:
    if file.endswith('png'):
        os.rename(f'images/{file}', f'images/{i}.png')
        i = i + 1
        print(file)