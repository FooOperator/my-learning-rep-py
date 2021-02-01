def mydecorator(function):
    def wrapper(*args):
        re_value = function(*args)
        print("I'm decorating")
        return re_value
    return wrapper

@mydecorator
def hello(person):
    return f"Hello {person}"


print(hello("Mike"))


