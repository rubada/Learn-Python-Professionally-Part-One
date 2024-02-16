# Python Closures
# As mentioned in Nested function (part 9), the inner function can't be accesed
# outside their enclosed scope, because the inner function object and its
# variables don't exsist in memory, they are exsit within the scope of the
# outer function object.
# That's why in the example below the inner function can't be called without
# calling the outer function, because it doesn't exsist in the outer scope.
def outerFunc(text):

    def innerFunc():
        return text
    return innerFunc()


# Call the inner function will raise a NameError
# print(innerFunc())

# To call the inner function the outer function has to be called
# print(outerFunc("hello"))

# What are Python Closure
# A closure is the process to remember the variables or values of the inner
# function (inside their enclosed scope) and access it, even if they don't
# exsist in the memory.
# To achieve the above instead of returning the inner function, the inner
# function object should be returned as shown below:
def outerFunc1(text):

    def innerFunc1():
        return text
    return innerFunc1


# assign the outer function to a varaible and print out the result
inner = outerFunc1("Hello World")
# print(inner)

# The return of the outer function is the inner function object, now the inner
# function object exsist outside its scope and its object is assigned to the
# variable inner, and the inner variable has a location in memory, to call the
# inner function (innerFunc1()), the inner variable should be called as shown
# below:
# print(inner())
# print(id(inner))


# Another example
def add_two_num(x):
    def add(y):
        return x + y
    return add


num = add_two_num(10)
# print(num(5))


# Why and when closures are used?
# 1. Can be used if there are few functions in the code, using closures to
# call them will provide elegant and clean code, but if there many function
# it is better to use classes with methods.

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
# modify them inside the inner function, in this case achieving our goal
# without changing the global variables, will provide a readable and clean
# code and the code will be easy to debug.
# 3. Closures are used in Python Decorators, as it will be discussed in
# section 4 later.
