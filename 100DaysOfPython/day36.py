try:
    ip = int(input('Enter a number: '))
    a = [1,2,3]
    print(a[ip])
except ValueError as e1:
    print('Value Error aala')
except IndexError as e2:
    print('Index Error aala')
except Exception as e:
    print(e)