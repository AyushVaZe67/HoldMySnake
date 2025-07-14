with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(5)

    data = f.read(11)
    print(data)
    print(f.tell())
    f.truncate(5)
    print(data)
