# Decorators
# To get any function name __name__ is used
def sub(a, b):
    return a - b


# print(sub.__name__)


def multiply(func):
    def mult_wrap(*args, **kwargs):
        """Hello this my decorator wrapper"""
        x = func(*args, **kwargs) * 10
        return x
    return mult_wrap


@multiply
def add(a, b):
    """This function return the sum of two functions"""
    return a + b


# Lets now use the __name__ with the add()
# print(add.__name__)
# print(add.__doc__)

# It will return the decorator wrapper name and docstrings to remove this
# issue Python provides the wrap decorator from the functool module to solve
# this issue @wraps takes a function to be decorated and allows to access the
# pre-decorated function’s properties in the decorator, such as the original
# function name, docstring, arguments list, etc...

from functools import wraps


def multiply1(func):
    """Hello this my decorator multiply1"""
    @wraps(func)
    def mult_wrap(*args, **kwargs):
        """Hello this my decorator wrapper"""
        x = func(*args, **kwargs) * 10
        return x
    return mult_wrap


@multiply1
def add1(a, b):
    """This function return the sum of two functions"""
    return a + b


print(add1.__name__)
print(add1.__doc__)

print(multiply1.__name__)
print(multiply1.__doc__)
