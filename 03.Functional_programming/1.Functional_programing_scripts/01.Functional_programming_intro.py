# Functional Programming is a programming paradigm, where functions can be
# used to solve problems.
# Python is an object-oriented programming language, also it does support
# functional programming.
# Functional programming characteristics:
# 1. Functions are first-class objects, which was discussed in the functions
# section part 7
# 2. Using recursive functions which were discussed in the functions section
# (part 11).
# 3. Pure functions, will return the same value when the function is called
# with the same arguments they have no side effects.
# Impure functions are functions that will not return the same value even if
# it is called with the same arguments, it may be affected by its outside.

# Pure function example:
def add(x, y):
    return x + y


# print(add(4, 5))


# Impure function example:
x = 7


def add1(y, z):
    return y + z + x


# print(add1(3, 4))

# If x is changed the function output will be changed, that is why add1
# function is an impure function.

# 4. Immutable data structures are the type of data used in functional
# programming. In the pass by object reference or by assignment part 6, (Python
# functions section), as mentioned there, the arguments variable will be
# changed in in the global scope if the arguments are updated inside the
# function if the arguments are mutable data structures.
# If immutable data structures are used then the variables' arguments in the
# global scope will not change, this will make the code easy clean, readable,
# easy to debug, and prevent changing the variables outside the function.

my_tuple = (1, 2, 5, 7)


def tuple_change(sequence_im):
    sequence_im = (3,) + sequence_im
    return sequence_im


# print(tuple_change(my_tuple))
# print(my_tuple)

# 5. Higher-order functions, are functions that take functions as arguments as
# an input, or/and return a function as an output. In the previous section
# (function section), it was shown that the function could take functions as
# arguments and return a function, such as function closure, also there are
# built-in functions in Python that can take functions as arguments which will
# be covered later in this section (map, filter, reduce, make_adder, and
# sorted), also Python decorators are higher-order functions, which will be
# covered late in a separate section.


# 6. Anonymous functions are functions without a name, in Python they are
# created using the lambda keyword, which also will be discussed later in
# this section.

# 7. List comprehensions are also used in many functional programming
# languages, and Python one of the languages that uses list comprehension,
# also will be discussed later in this section.
