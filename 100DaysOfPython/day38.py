a = int(input('Enter between 0 to 10: '))
if a > 10:
    raise ValueError('Enter a number')
else:
    print('OK thanks for : ',a)