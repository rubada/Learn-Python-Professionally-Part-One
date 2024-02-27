# Decorators with arguments
# As shown in the previous section when using decorators, the decorator will
# only take a single parameter in the outer_decorator, and this parameter is
# the function that the decorator is used on, and the parameters in the
# inner_decorator will modify this decorated function and these parameters are
# the function's parameters, as shown below:

def outer_decorator(func):

    def inner_decorator(*arg, **kwargs):

        return_func = func(*arg, **kwargs)
        return return_func

    return inner_decorator


@outer_decorator
def function_ex(parameters):
    pass


# Let's check what will happen if other parameters are used instead of the
# function:
def string_deco(a, b):
    def wrapper(func):
        x = f"{func()}. {a} {b}"
        return x
    return wrapper


# This how the decorator with arguments is written:
@string_deco("This is", "a Python course")
def string_func():
    return "Hello"


# print(string_func())

# When calling the function as shown above, it will return an error, because
# the function is being called string_func() and has a value (Hello), then
# inside the wrapper the "Hello"() will be called, that's why Python raised
# TypeError: 'str' object is not callable.
# To solve this the function object should be called as shown below:
# print(string_func)


# Another example
def num_deco(a, b):
    def wrapper(func):
        x = func() + a + b
        return x
    return wrapper


# This how the decorator with arguments is written:
@num_deco(2, 4)
def num_func():
    return 7


# print(num_func())
# print(num_func)


# If the function has parameters when calling the function object, as
# mentioned above, then the arguments can't be assigned to the function
# object and this will raise an error as shown below:

# @string_deco("This is", "Python course")
# def string_funcp(x):
#     return "Hello"


# print(string_funcp)


# But how can more parameters or arguments be added to a decorator, and call
# the function with its parameter?
# To solve the above issue the decorator should have three nested functions,
# as shown below:
def string_deco1(a, b):
    def inner_deco(func):
        def wrapper(*args, **kwargs):
            x = f"{func(*args, **kwargs)}. {a} {b}"
            return x
        return wrapper
    return inner_deco


@string_deco1("This is", "a Python course")
def string_func1(x):
    return "Hello" + " " + x


# print(string_func1("World"))


# Another example:
def multiply_add(x, y):
    def inner_deco(func):
        def wrapper(*args, **kwargs):
            z = func(*args, **kwargs) * 10 + x + y
            return z
        return wrapper
    return inner_deco


@multiply_add(2, 3)
def add(a, b):
    return a + b


# print(add(1, 2))


# This is the same as follows:
def add1(a, b):
    return a + b


result = multiply_add(2, 3)(add1)
print(result(1, 2))

# There is also class decorator, which adds a class as decorator to a function,
# and it provides a clean code when using parameters.
