# What is an if-statement?
# If-statement is a condition expression,  where the output of this condition
# expression is either True or False, the are many Python objects that
# return True or False, and they can be used with if statement such as:
# 1. Comparison Operators (==, !=, >, <, >=, <=)
# 2. Logical Operators (and, or, not)
# 3. Identity Operators (is, is not)
# 4. Membership Operators (in, not in)
# 5. Many methods and functions (isinstance(), any(), all())
# 6. Also empty "", [], {}, () and 0 return False, and the opposites return
# True

# How to use if-statement?
a = 400
b = 800

# print(f"a = {a} ", f"b = {b}", sep="\n")

if a < b:
    a = a + b
    # print(f"new a = {a}")

# or if there are other conditions to be satisfied, "else" can be used.
# a now equal 1200

# print(f"a = {a} ", f"b = {b}", sep="\n")

if a < b:
    a = a + b
    # print(f"new a = {a}")
else:
    b = b + 70
    # print(f"new b = {b}")

# or if there are more than two condition then "elif" is used.
# a = 1200 and b = 870 after using above condition

c = 674
print(f"a = {a} ", f"b = {b}", f"c = {c}", sep="\n")


if a < b:
    a = a + b
    print(f"new a = {a}")
elif b < c:
    b = b + 70
    print(f"new b = {b}")
elif c > a:
    c = a + b
    print(f"new c = {c}")
