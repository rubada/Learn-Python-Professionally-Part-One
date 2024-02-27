# 1st Question
# Write a decorator that when used on a recursive function returns the
# function name, docstrings, and function arguments as a result.
# Use the following function
# def factorial(x):
#     """This function returns the factorial number of the input
#     Inputs
#        x is an integer number
#     return
#        Factorial of a number as integer number"""
#     if x == 0:
#         return 1
#     return x * factorial(x-1)

# The output should be as follows:

# The function name is factorial
# The function docstring is:
# This function returns the factorial number of the input
#     Inputs
#        x is an integer number
#     return
#        Factorial of a number as an integer number
# Factorial value = 24


# Solving this problem a memoize decorator.
# One advantage of memoize decorator it can drastically cut down the
# computational time of the function’s output, especially when using a function
# such as the factorial function that consumes memory and CPU power.
# Check memoize_decorator.py in the Decorators_exercises_solutions folder, to
# get an idea of how they work.

def memoize_dec(func):
    fact = {}

    def wrapper(*args, **kwargs):

        # When calling the function using the decorator, use the below
        # statement will check if the function output is stored in the fact
        # dictionary or not, if the value is stored the decorator will return
        # the result, if not it will use the below statement to store it in
        # the fact dictionary.

        key = (*args, *kwargs.items())

        if key not in fact:
            fact[key] = func(*args, **kwargs)

            # to check if the decorator prints the values from the fact
            # dictionary or not check with the below print
            # print("not in fact")

        if not key[0]:
            print(f"The function name is {func.__name__}")
            print(f"The function docstring is:\n{func.__doc__}")

        return fact[key]
    return wrapper


@memoize_dec
def factorial(x):
    """This function returns the factorial number of the input
    Inputs
       x is an integer number
    return
       Factorial of a number as an integer number"""
    if x == 0:
        return 1
    return x * factorial(x-1)


result = factorial(4)
result1 = factorial(x=5)
# print(f"Factorial value = {result}")
# print(f"Factorial value = {result1}")

result_m = factorial(4)
result1_m = factorial(5)
# print(f"Factorial value = {result_m}")
# print(f"Factorial value = {result1_m}")


# 2nd Question
# Write a decorator to validate the function arguments as integers, if
# arguments are not integers the decorator should return a message that
# the arguments should be integers.
# Use the following function:
# def fibonacci_nums(x):
#     fibo = []
#     n = 2
#     fibo.append(0)
#     fibo.append(1)
#     fibo.append(1)
#     while x != n:
#         n = n + 1
#         fibo.append(fibo[n-1] + fibo[n-2])
#     return fibo

def integer_check(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(num, int) for num in args):
            return "Arguments should be of integer type"

        elif not all(isinstance(num, int) for num in kwargs.values()):
            return "Keyword arguments should be of integer type"
        else:
            return func(*args, **kwargs)
    return wrapper


@integer_check
def fibonacci_nums(x=6):
    fibo = []
    n = 2
    fibo.append(0)
    fibo.append(1)
    fibo.append(1)
    while x != n:
        n = n + 1
        fibo.append(fibo[n-1] + fibo[n-2])
    return fibo


# print(fibonacci_nums(4))
# print(fibonacci_nums(x=4.5))
