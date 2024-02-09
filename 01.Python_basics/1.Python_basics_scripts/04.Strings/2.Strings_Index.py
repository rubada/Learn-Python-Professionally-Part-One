"""Indexing is about how to access a specific element in a string, list, tuple,
set, etc., using its position or index number"""

# Indexing in Python starts at zero not at one

a = "Hello World"
print(a[0])
print(a[10])
print(a[6])
print(a[5])

# len() function, returns the length of a string or list or tuple, etc.
b = len(a)
print(b)

# using for loop
for i in range(b):
    print(a[i])

for i in a:
    print(i)
