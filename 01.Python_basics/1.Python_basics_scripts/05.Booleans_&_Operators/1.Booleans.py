# Booleans
# Booleans return two values, True or False
# Boolean often used in if else statements, which will be covered later.
# in the future

# Examples
x = 4
y = 3
z = 9
# print(x > y)
# print(z == x)
# print(y < z)
# print(9 == 9)

# We can use the bool() function to check for "True" or "False"
# Almost every object in Python returns "True", unless they are 0 or an
# empty objects, such as (emplty strings, empty lists, empty dictionaries,
# etc.), which they will return "False", as shown below:

# All strings return True value unless it is not an empty string:
# print(bool("Ruba"))
# print(bool(""))
# print(bool(" "))
# print(bool("55$3"))

# All numbers return True value unless it is 0:
# print(bool(0))
# print(bool(99))
# print(bool(1))

# Any list, set, tuples, dictionary return True value unless it is empty:
a = ["a", 3]
b = []
print(bool(a))
print(bool(b))
