# Decorators
# Decorators are functions that considered first class object, which discussed
# in part 7 in the functions section
# Decorators are functions that return other function, and have functions as
# an arguments.
# Decorators are higher order functions.
# Decorators are closures that are very powerful and used to modify the
# functionality of other functions. Which means they are used to wrap another
# function, and then extend the functionality (modify) without changing the
# function.
# Decorators Syntax, the inner function is called a wrapper
def outer_decorator(func):

    def inner_decorator(*arg, **kwargs):

        return_func = func(*arg, **kwargs)
        return return_func

    return inner_decorator


# Lets take an example
# How decorators are used?
# To call a decorator the @ is used before the decorator name and then it will
# be assigned before the function as shown below

def multiply(func):
    def wrapper():
        x = func() * 10
        return x
    return wrapper


@multiply
def digits():
    return 5


# print(digits())


# This is equal to calling a function with another function as its parameter
def digits1():
    return 5


mutli = multiply(digits1)
# print(mutli())

# This covered in Python_closure part 10 in the functions sections
