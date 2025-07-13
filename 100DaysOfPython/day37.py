def func1():
    try:
        l1 = [1,2,3,4,5,6]
        i = int(input('Enter index: '))
        print(l1[i])
        return 1
    except:
        print('Error')
        return 0
    finally:
        print('I am always executed')

print(func1())