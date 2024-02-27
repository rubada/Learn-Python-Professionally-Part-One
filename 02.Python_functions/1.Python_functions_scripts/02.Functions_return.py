# Functions
def fun_func():
    print("This is my first Function")


# If the above function is assigned to a variable without parentheses,
# function reference or object is assigned to the variable, and both have the
# same location in memory, (same object).

a = fun_func

# In this case when calling the variable by adding the parentheses to it, then
# the variable will invoke or call the function because they are the same
# object.

# a()
# print(id(fun_func))
# print(id(a))


# Beware that using the print() function inside the function, will not return a
# value, if the return keyword is not used in the function, None will be
# returned.

def add():
    a = 3 + 4
    print(a)


# b = add()
# b
# c = b + 5
# print(c)


# To solve the above return keyword should be used:
def add1():
    a = 3 + 4
    return a


d = add1()
e = d + 5
print(d)
print(e)
