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
