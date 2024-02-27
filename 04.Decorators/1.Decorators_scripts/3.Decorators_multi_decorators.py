# Decorators
# Multiple decorators can be used to wrap one function.

def multiply_add(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs) * 10 + 5
        return x
    return wrapper


def division(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs) / 2
        return x
    return wrapper


@multiply_add
@division
def add(a, b):
    return a + b


# print(add(2, 5))


# Same as
def adding(a, b):
    return a + b


divide_num = division(adding)
mutli_add_num = multiply_add(divide_num)
# print(mutli_add_num(2, 5))


@division
@multiply_add
def add1(a, b):
    return a + b


# print(add1(2, 5))


# It is the same as
def adding1(a, b):
    return a + b


mutli_add_num = multiply_add(adding1)
divide_num = division(mutli_add_num)
# print(divide_num(2, 5))


# Beware when using more than one decorator on a function to take into account
# the  order of the decorators, which will wrap the function first, second,
# third, etc., as shown below:

# @etc.
# @third
# @second
# @first
# def func(a, b):
#     return a + b
