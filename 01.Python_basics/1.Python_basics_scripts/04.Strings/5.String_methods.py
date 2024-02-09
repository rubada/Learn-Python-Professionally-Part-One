# String Mothods
# They are buitl-in methods used for string modifying or return True or False,
# we will learn most used methods.
# To know more about these mehtods check Python documentation or any other site
# that you prefer:
# https://docs.python.org/3/library/stdtypes.html#string-methods

a = "Python is a Wide. used Programming. Language"

# Note, methods (for lists, strings, dictionary etc.) are written on the right
# side of the object after the ".", as shown in below syntax:
# object.method()

# 1. uppercase() metthod:
# print(a.upper())

# 2. lowercases() method:
# print(a.lower())

# 3. replace() method, it is better to modify the string to lower or upper
# case and then apply replace method because python is case sensitive.
# print(a.replace("P", "L"))
# print(a.replace("Python", "Java"))

# 4. split() method
# print(a.split())
# print(a.split("."))
# print(a.split('. '))


# 5. strip() method
b = "   Python    "
c = ",,,fffgj....Python   l"
# print(b.strip())
# rint(c.strip(",gj. l"))


# 6. join() method
d = ["I", "love", "Python"]
# print(" ".join(d))


# 7. islower() mehtod:
e = "pYthon"
# print(e.islower())
