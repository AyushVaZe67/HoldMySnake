def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5)+ 1 , 2):
        if num % i == 0:
            return False
    return True



l1 = [2,3,4,5,6,7,8,9]
for i in range(len(l1)):
    if is_prime(l1[i]):
        print(f'{l1[i]} IS PRIME')
    else:
        print(f'{l1[i]} IS NOT PRIME')