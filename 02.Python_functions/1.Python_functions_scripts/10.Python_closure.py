# Python Closure
# As mentioned in the Nested functions (part 9), the inner function can't be
# accessed outside their enclosed scope, because the inner function object and
# its variables don't exist in the memory, they exist within the scope of the
# outer function object.
# That's why in the example below the inner function can't be called without
# calling the outer function, because it doesn't exist in the outer scope.

def outerFunc(text):

    def innerFunc():
        return text
    return innerFunc()


# Call the inner function will raise a NameError:
# print(innerFunc())

# To call the inner function the outer function must be called:
# print(outerFunc("hello"))


# What is Python Closure?
# A closure is the process of remembering the variables or values of the inner
# function (inside their enclosed scope) and access it, even if they don't
# exist in the memory.
# To achieve the above instead of returning the inner function, the inner
# function object should be returned as shown below:
def outerFunc1(text):

    def innerFunc1():
        return text
    return innerFunc1


# Assign the outer function to a variable and print out the result:
inner = outerFunc1("Hello World")
# print(inner)

# The return of the outer function is the inner function object, now the inner
# function object exists outside its scope and its object is assigned to the
# variable inner, and the inner variable has a location in the memory, to call
# the inner function (innerFunc1()), the inner variable should be called as
# shown below:

# print(inner())
# print(id(inner))


# Another example
def add_two_num(x):

    def add(y):

        return x + y
    return add


num = add_two_num(10)
# print(num(5))


# Why and when closure are used?
# 1. a closure can be used if there are few functions in the code, using a
# closure to call them will provide elegant and clean code, but if there are
# many functions it is better to use classes with methods.

def func(z):

    def multiply(x, y):
        return x * y * z

    def division(x, y):
        return x / y

    return multiply, division


multi_num, divide_num = func(10)
# print(f"multi_num = {multi_num(3, 5)}\ndivide_num = {divide_num(15, 3)}")


# 2. Instead of defining the global variables outside the function, using
# closure to define nonlocal variables inside the outer function, and then
# modyfy them inside the inner function, in this case achieving our goal
# without changing the global variables, this will provide a readable and
# clean code and the code will be easy to debug.


def add_two_num():
    x = 6

    def add(y):
        nonlocal x
        x = x + y
        return x
    return add, x


number, x = add_two_num()
# print(number(3))
# print(x)


# if the inner function is called in the return statement
def add_num():
    x = 6

    def add():
        nonlocal x
        x = x + 1
        return x
    return add(), x


number1, x1 = add_num()
# print(number1)
# print(x)

# 3. Closure is used in Python Decorators, as it will be discussed in
# section 4 later.
