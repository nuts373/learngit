import functools
def log(text = None):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(args, **kw):
                if text == None:
                    print('call %s():' %func.name)
                else:
                    print('%s %s():' %(text, func.name))
                return func(args, **kw)
            return wrapper
        return decorator

@log()
def now1():
    print('2015-9-15')
@log('test')
def now2():
    print('2015-9-15')
print(now1())
print(now2())