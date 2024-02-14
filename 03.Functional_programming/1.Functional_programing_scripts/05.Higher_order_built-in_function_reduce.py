# Higher-order built-in functions
# As mentioned before these function can accept function as their arguments and
# or return function as an output.
# reduce()
# is used to apply a function of two arguments cumulatively to the items
# of an iterable and reduce the iterable to a single value.
# Syntax
# reduce(func, iterable[, initial])
# initial is a value that is used as initial value to start with when using
# reduce().
# In order to use reduce() the functools buitl-in module should be imported,
# modules will be discussed later in a seperate section
# Example to find the sum:
from functools import reduce
num = [2, 6, 7, 9, 3]
sum_list = reduce(lambda x, y: x + y, num)

# print(sum_list)

# same as sum(function can be used)
# print(sum(num))


# or the multiplication
def multiplication(a, b):
    return a * b


# 3 is the intial value in which the multiplication will start with
mult_list = reduce(multiplication, num, 3)

# print(mult_list)

# same as
a = 3 * 2 * 6 * 7 * 9 * 3
# print(a)
