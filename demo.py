def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper


@uppercase_decorator
def say_hi():
    return 'hello there'

s=say_hi()
print(s)