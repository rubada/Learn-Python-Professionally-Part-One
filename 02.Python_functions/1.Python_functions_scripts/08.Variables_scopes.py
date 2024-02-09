# Scope of variables is the location or the region where the variables can be
# accessed.
# There are three types of varibles scopes
# 1. Local Scope
# 2. Global Scope
# 3. Nonlocal Scope
# Nonlocal scope will be covered in Nested functions

# Local Scope
# Local scope is the region inside the function where the variables are defined
# and accessed, these local variables can be only accessed within the function.
def add(x):
    y = 10
    return x + y


adding = add(3)
# print(adding)
# print(y)

# As shown above print(y) raise an error, because y is variable defined within
# the function, it can't be accessed outside the function


# 2.Global Scope
# Global scope is the region outside the function or the class where the
# variables are defined, that means the global variables can be accessed inside
# and outside the function or the class.


# 1. Accessing global variable from inside a function
def message():
    print("Printing the global text inside the Function", text)


text = "Hello world"
# print("Printing the global text outside the Function", text)

# Calling the function
# message()


# 2. Local and Global varaibles have the same name
# What if both variables have the same name?
def message1():
    text1 = "I'm having fun"
    return text1


text1 = "Hello world"
# print(message1())
# print(text1)

# As mentioned above in local scope, local variables can be accessed only
# inside the function, and both variables are two different objects, thus
# their values will not change.


# 3. Modifying global variable from inside the function will raise an error.
# If x is not changed, no error, and the variable can be accessed as discussed
# in points 1.
# let's check the example below:

# def subtract_num():
#     x = 7 - x
#     return x


# x = 5
# sub = subtract_num()
# print(sub)
# print(x)


# It will raise an error saying local variable cannot be accessed, which means
# that python is trying to access x as local variable and raised an error
# because x has no value.

# How to solve this?
# To change or reassigned variables, Python should be told that this variable
# or variables are global, and this is done by using the global keyword.
def subtract_num():
    global x
    x = 8 - x
    return x


x = 5
sub = subtract_num()
# print("Variable changed inside the function", sub)
# print("Variable changed outside the function", x)

# x will be changed in the global scope, becuase using global keyword will
# change the variable outside the function, (even if the object is immutable),
# so beware when using global keyword to change or reassigned the varaibles.

# It is recommended to minimize the use of global variables because eccessive
# using of global variable within many functions inside the code, it will make
# the code difficult to understand and debug.


# Important note: there are two ways to change global variables within the
# function:
# 1. Using global keyword, the variable will changed even if it is mutable or
# immutable.
# 2. As discussed in part 6 (pass by object reference or pass by assignment)
# if the variable is mutable.

# Thus one must be careful when dealing with global variable


# Global varaible are used accross python modules, check example in folder
# global_variable_example, on how to use global variables accross modules.
