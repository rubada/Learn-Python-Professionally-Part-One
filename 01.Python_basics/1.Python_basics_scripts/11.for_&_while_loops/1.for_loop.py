# for loop
# A for loop is used to iterate on an iterable, such as lists, tuples,
# sets, dictionaies and strings etc.
my_string = "This a Python course"
# for letter in my_string:
#     print(letter)

# or use indexing to loop over the string
# for i in range(len(my_string)):
#     print(my_string[i])

# or a list
my_list = my_string.split()
# print(my_list)

# for item in my_list:
#     print(item)

# or use indexing to loop over the list
# for i in range(len(my_list)):
#     print(my_list[i])


# As Shown above range() function can be used in for loop
# len() function, range can be used in diffferent ways
# range(start, stop-1, step)
# for i in range(10):
#     print(i)

# range(start, stop-1, step)
# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 3):
#     print(i)

# for loop can be used with if statment
my_list = ['This', 'a', 'Python', 'course']

for item in my_list:
    if item == "Python":
        print("Python is True")
    else:
        print(item)
