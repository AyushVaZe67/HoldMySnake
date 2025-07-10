def func1():
    try:
        l1 = ['a','v','w']
        i1 = input('Enter a index: ')
        print(l1[int(i1)])

    except Exception as e:
        print(e)

    finally:
        print('Always executed!!!')

func1()