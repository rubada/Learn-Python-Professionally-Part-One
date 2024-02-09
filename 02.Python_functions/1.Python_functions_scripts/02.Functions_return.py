# Functions
def fun_func():
    print("This is my first Function")


# If above function is assigned to a variable without parentheses, the function
# reference or object is assigned to the variable, and both have the same
# location in memory, (same object).
a = fun_func

# in this case when calling the varuable by adding the parentheses to it, then
# the variable will invoke or call the function because they are the same
# object.
# a()
# print(id(fun_func))
# print(id(a))


# Beaware that using print() function inside the function, will not return a
# value, if return keyword is not used in the function, None will be returned.
def add():
    a = 3 + 4
    print(a)


# b = add()
# b
# c = b + 5
# print(c)


# to solve the above return ketword should be used
def add1():
    a = 3 + 4
    return a


d = add1()
e = d + 5
print(d)
print(e)
