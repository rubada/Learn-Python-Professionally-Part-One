# # Functions
# What are functions?
# A Function is a block of different expressions that return a specific
# task.
# Functions are used when a specific task is required more than one time
# in the code, to prevent repeating this task inside the code a function is
# used to return this task.
# There are three types of functions in Python:
# 1. Built-in function, which will be covered in functional programming
# section
# 2. lambda function, which will be covered in functional programming
# section
# 3. User-defined function, which will be covered in this section
# Functions advantages:
# 1. Code Readability will be increased
# 2. Code Reusability will be increased
# Difference between arguments and parameters:
# A parameter or formal parameters are the variables listed inside the
# parenthesis in the function definition. A function can have many arguments
# and they are separated by commas.
# Arguments or actual parameters are values that are passed in the function
# parenthesis.
# Let's Take an example to explain the above.

def fun_func():
    print("This is my first Function")
    # return "hello"


# Here calling or invoking the function will return an output because print()
# function is used inside the function block.
# To call a function, parentheses should be used to get the result.
# fun_func()

# using print() as shown will return the function output and None

print(fun_func())
