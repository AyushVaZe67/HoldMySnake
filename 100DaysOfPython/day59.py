def greet(f1):
    def mfx(*args, **kwargs):
        print('GM')
        f1(*args, **kwargs)
        print('Thanks for using this function')
    return mfx

@greet
def hello():
    print('Hello')

@greet
def add(a,b):
    print(a+b)

# hello()
add(11,22)