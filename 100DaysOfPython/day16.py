age = int(input('Enter a age : '))
match age:
    case 18:
        print('18 saal')
    case 21:
        print('21 saal')
    case _:
        print('NO saal')