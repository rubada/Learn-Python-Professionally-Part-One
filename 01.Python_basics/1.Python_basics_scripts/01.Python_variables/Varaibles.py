# To define what variables are, let's take an example from real life, let's
# say you have a new friend, and you want to get his contact details, such as
# his name, phone number, address, etc., if want to memorize these details,
# there is a chance that you can forget them, but if you save them in your
# phone, under your friend's name, then you can save them forever.
# This is the same as the variable in coding, where the objects (data,
# functions, classes, etc.) are assigned to a name, and then the code can use
# this variable inside, without the need to define it every time.
# Also, data or values inside the variables may change, which is why they are
# called variables.
# This leads us to the variables’ definition, which is, that variables are
# temporary containers to store data.


# To define a variable, use the "=" to assign any type of data to a specific
# name
first_name = "John"
last_name = "Sterling"
phone_number = 46788389
address = "anywhere street no. 15"
weight_kg = 50.9

# Variables are especially important in any programming language because any
# type of data or objects in Python can be stored in the variables. Then
# variables can be used inside the code to achieve the code purpose.
# Using variables will allow the programmer to change variables where they are
# defined, thus they will be changed at any position they are used in the code.
# For example, getting the full name of a person.

full_name = first_name + " " + last_name

# or changing the weight from kg to lbs
weight_lbs = 2.2046 * weight_kg

# print(full_name)
# print(weight_lbs)


# To define variables certain rules should be followed:
# These rules can be applied to any name defined in Python such as functions
# and class names etc.
# 1. Variables should start with a letter or underscore "_"
_number = 55

# 2. After the letter or the underscore, letters, numbers, or "_" can
# be added.

n1 = 3.5
n_1 = 8

# Beware, to define a variable letters, numbers, and "_" are used, numbers
# shouldn't be used as the first character in a variable name.
# The same rule applies to any name defined in Python.

# 3n = 5
# n+time = 7
# hour@min = 66

# 3. In Python when defining any object with a name, (variables, classes,
# functions etc.), it should be taken into account that Python is
# case-sensitive, let's take an example:
my_name = "John"
my_nAme = "Mary"

# my_name and My_name are two different variables (objects).
# print(my_name)
# print(my_nAme)

# as shown above the print function is written in small letters, what will
# happen if it is written with capital letters:
# PRINT(my_name)
# Print(My_name)


# To prevent errors when writing code, built-in objects should be written as
# they are defined inside Python, otherwise errors will be raised.

# 4. When defining a variable, the name given to it should be readable
# and spaces are not allowed.
my_name = "John"
My_name = "Mary"
MyName = "Lilly"
# My Name = "Tom"

# Variables should be descriptive, anyone who reads the variable should know
# what this variable is about and where it should be used.
rectangular_width = 5
rectangular_length = 10
rectangular_area = rectangular_width * rectangular_length

# print(rectangular_area)
