def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    total = sum(int(digit) ** n for digit in num_str)
    return total == num


num1 = int(input('Enter a number: '))
print(is_armstrong(num1))