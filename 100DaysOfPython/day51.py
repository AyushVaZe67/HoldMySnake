with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(5)

    data = f.read(15)
    print(data)
