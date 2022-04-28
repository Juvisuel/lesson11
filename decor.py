def decor_all(f):
    def inner(*args, **qwargs):
        print('*' * 100)
        result = f(*args, **qwargs)
        print('*' * 100)
        return result
    return inner