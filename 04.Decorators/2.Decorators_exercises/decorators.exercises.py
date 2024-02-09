# Question 1
# Write a decorator that when used on a recursive function returns the
# function name, docstrings and the function result.
# Use the follwing function
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
#        Factorial of a number as integer number
# Factorial value = 24


# Question 2
# Write a decorator to validate the function arguments as integers, if
# arguments are not integer the decorator should return a message that
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
