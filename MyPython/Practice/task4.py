num1 = int(input('Enter a number 1: '))
num2 = int(input('Enter a number 2: '))
num3 = int(input('Enter a number 3: '))

if num1 > num2 & num1 > num3:
    print(f'{num1} is largest')
elif num2 > num1 & num2 > num3:
    print(f'{num2} is largest')
else:
    print(f'{num3} is largest')