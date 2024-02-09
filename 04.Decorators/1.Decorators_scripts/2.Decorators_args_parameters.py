# Decorators
# How to use decorators with parameter?
# The number of parameters in the wrapper should be the same as the number
# of parameters in the function as shown below

def multiply0(func):
    def wrapper(a, b):
        x = func(a, b) * 10
        return x
    return wrapper


@multiply0
def adding(a, b):
    return a + b


# print(adding(3, 5))


# The above decorator will only used with functions that have two parameters,
# in this case this decorator use will be limited.
# Then how can the decorators be used with functions that has different number
# of parameters?
# This can be solved by using arbitrary arguments (*args and **kwargs) inside
# the wrapper function, in this case the decorator will be used with many
# functions regardless of the number of parameters or even functions that don't
# have parameters. As shown in below example:


def multiply(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs) * 10
        return x
    return wrapper


@multiply
def add(a, b):
    return a + b


# print(add(2, 5))


@multiply
def sub(a, b, c):
    return a - b - c


# print(sub(10, 3, 5))


@multiply
def digits():
    return 4.7


# print(digits())

# As shown above the multiply decorator is used with different functions which
# have different number of parameters, because of the use of arbitrary
# arguments inside the wrapper
