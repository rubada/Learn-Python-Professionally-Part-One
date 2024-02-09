# String slicing is a method to create sub-string from the original string.

a = "Hello World"

# Slicing rules:
# a. a[start:stop]
# Indexing will begin from "start" through "stop-1".

# print(a[3:8])
# print(a[-4:-1])

# b. a[start:]
# Indexing will begin from "start" to the end of the string.

# print(a[4:])
# print(a[-4:])

# c. a[:stop]
# Indexing starts from the beginning through "stop-1".

# print(a[:7])
# print(a[:-7])

# d. a[:]
# Create a copy of the string or array.

# print(a[:])
# print(a[::])


# e. a[start:stop:step]
# Indexing will begin from "start" through "stop-1", taking in account
# the step.

# print(a[2:10:2])
# print(a[-7:-3:2])

# f. reverse order
# a[start:stop:-step]
# "start" index > "stop" index, begin from "start" through "stop+1" in
# descending order.
# As shown above step is a negative number, indicating that the list output
# will be reversed.

# print(a[::-1])
# print(a[8:3:-1])
# print(a[8:3:-2])
# print(a[-2:-9:-2])
# print(a[3::-1])
# print(a[:6:-1])
