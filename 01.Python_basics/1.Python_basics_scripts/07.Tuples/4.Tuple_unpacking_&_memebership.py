# Using memebership operators with tuples
my_tuple = (9, "cat", 9.7, "dog", [False, True, None], 9, (4, 1, "orange"))

# if "cat" in my_tuple:
#     print("True, cat is in my Tuple")
# if "mouse" not in my_tuple:
#     print("False, mouse is not in my Tuple")


# Tuples unpacking
# There are two ways to assign objects in a tuple to variables.
# 1. Using Index
new_tuple = (1, 3, 9, 8, 4, 0, 2)
a = new_tuple[0]
b = new_tuple[1]
c = new_tuple[2:6]
d = new_tuple[6]

# print(a, b, c, d, sep="\n")

# Sequence unpacking
a1, b1, c1, *d1 = new_tuple
print(a1, b1, c1, d1, sep="\n")
