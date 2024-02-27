# Higher-order built-in functions
# As mentioned before these functions can accept a function or functions as
# their arguments and/or return a function or functions as an output.
# reduce()
# The reduce() is used to apply a function of two arguments cumulatively to
# the items of an iterable and reduce the iterable to a single value.
# Syntax
# reduce(func, iterable[, initial])
# initial is a value that is used as the initial value to start with when using
# reduce().
# To use reduce() the functools built-in module should be imported,
# modules will be discussed later in a separate section
# Example to find the sum:

from functools import reduce
num = [2, 6, 7, 9, 3]
sum_list = reduce(lambda x, y: x + y, num)

# print(sum_list)

# Same as the sum() function, and it will give the same result:
# print(sum(num))


# or the multiplication
def multiplication(a, b):
    return a * b


# 3 is the initial value in which the multiplication will start with:
mult_list = reduce(multiplication, num, 3)

# print(mult_list)

# same as
a = 3 * 2 * 6 * 7 * 9 * 3
# print(a)
