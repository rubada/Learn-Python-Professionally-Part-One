# Escape Characters:
# Are used to insert special charaters lines etc. into a string or code by
# using \ Backslash.
# There are many escape characters used in Python, and we will discuss the
# most used.
# There are mnay sites explain the esacpe characters in python, and show
# how to use them, you can check them out.
# 1. \" or \'
# The back slash is used to allow us use single or double quotes inside the
# string as shown below:
a = 'I\'m taking this python course'
# print(a)

b = "This course is about \"Python\""
# print(b)

# Using differnet quotes (single or doubles) as string quotes and quotes inside
# the string, will not give and error as shown below.
# c = "This course is about 'Python'"
c = 'This course is about "Python"'
# print(c)

# 2. \n used to add a new line
# Using it inside a string
d = "This course is about\nPython"
# print(d)

e = "My name is"
f = "Ruba"
sent = e + ":" + "\n" + f
sent1 = f"My name is \n{f}"
# print(sent)
# print(sent1)

# Or using it in print function
# print("\n")
# print(e, "\n", f)

# 3. \t used to create a tab
sent2 = f"My name is \t {f}"
print(sent2)
print(e, "\t", f)
