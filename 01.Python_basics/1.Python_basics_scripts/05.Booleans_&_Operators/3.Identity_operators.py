# Identity Operators
# Data in Python are represented by objects.
# Each object has an identity, value, and type.
# For example:
a = "Python"
# "a" has a string type and value of python, then what is the identity?
# Object identity is the object address in memory, each object has a memory
# location once it is created.

# Identity operators are special comparison operators, used to compare if two
# variables have the same object in memory.
# They don't compare the values of the variable like the equal operator ==
# but compare the memory address.

# There are two identity operators:
# "is" returns True if both variables are the same object and have the same
# memory address, and False if not.
#  "is not" return True if both variables are not the same object and don't
# have the same memory address, and False if not.
# Identity operators work with different types of objects such as strings,
# lists, numbers, tuples, etc.
# To check the memory address we use the id() function.

# Identity operators and functions are important when working with large
# data structures because they lead to conserving memory. How?
# Example:

b = [6, 3]
c = [6, 3]
d = b
# print(b == c)
# print(b is c)
# print(d is b)

# d = b is not a proper way to copy a list because d and b are the same object,
# any change in d will affect b.
# d.append(5)
# print(b)
# print(d)


# Mutable Objects such as lists, dictionary, sets, adding or removing values
# to them will not change them to another object.
list1 = [2, 4, 6]
# print(list1)
# print(id(list1))

# list1.append(9)
# print(list1)
# print(id(list1))

# Imutable Objects such as Nummbers, strings, tuples, will change to
# another object, such as using concatenating in strings or
# using assignment Operators in numbers calculation
# example
e = "hello"
# print(e)
# print(id(a))

e = e + " " + "world"
# print(e)
# print(id(e))

f = 5
# print(f)
# print(id(f))

f += 2
# print(f)
# print(id(f))
