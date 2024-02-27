# There are three types of numbers
# 1. Integers
# 2. Floats
# 3. Complex Numbers

# What we will learn?
# We will learn also about the type() function.
# We will learn about casting.

x = 88
y = 6.8
z = 1+6j

# print("x Type:", type(x))
# print("y Type:", type(y))
# print("z Type:", type(z))

# To change a float to integer, use the float() and int() constructors or
# functions

a = float(x)
# print(a)
# print("a Type:", type(a))

b = int(y)
# print(b)
# print("b Type:", type(b))

'''We can't cast a complex number to int or float
uncomment below the line and run code will give a type error'''
# c = int(z)

# print(c)

# To convert float or integer to complex number use the complex() function.
d = complex(x)
# print(d)
# print("d Type:", type(d))

e = complex(y)
# print(e)
# print("e Type:", type(e))


# Changing a string to float or integer
num_str = "5"
float_num = float(num_str)
# print(float_num)
# print("float_num Type:", type(float_num))

# or change it to int
int_num = int(num_str)
# print(int_num)
# print("int_num Type:", type(int_num))

# But if the string is a float number, using int() will raise ValueError,
# this error will be raised if an object cannot be converted to an integer,
# as shown in the below example.
flot_str = "3.4"
# print(int(flot_str))

# int() function or constructor, the syntax is as follows:
# int(x, base=10), to convert the string to an integer and apply base 10 on
# it, the string should be integer not float otherwise an error will be raised,
# to solve this issue first change the number to a float then to an integer.

# Other bases such as 2 for a binary system, can be converted to an integer.
binary_num = "1101"

# print(int(binary_num, 2))
