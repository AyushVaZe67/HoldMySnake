try:
    ip = int(input('Enter a number: '))
    print(ip+1)
except Exception as e:
    print(e)
finally:
    print('Khatam')