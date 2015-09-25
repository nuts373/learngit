def deco(func):
    def wrapper():
        print("begin")
        func()
        print("end")
    return wrapper

@deco
def myfunc():
    print("myfunc called")

myfunc()