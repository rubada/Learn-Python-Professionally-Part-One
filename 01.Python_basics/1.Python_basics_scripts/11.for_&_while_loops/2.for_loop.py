# "for" loop
my_list = ['This', 'a', 'Python', 'course']

# "break" statement can be used with for loop if the condition is satisfied

# for item in my_list:
#     if item == "Python":
#         print("Python is True")
#         break

# In below example the loop is broken after the condition is satisfied
x = 0
# for item in my_list:
#     x += 1
#     if item == "Python":
#         break
#     print(f"The condition is not satisfied {x}")

# If an output is required then continue statement should be used
# for item in my_list:
#     x += 1
#     if item == "Python":
#         continue
#     print(f"Python is not True {x}")

# "else" can be used with for loop
# for item in my_list:
#     if item == "Python":
#         print("item is Python")
# else:
#     print(item)

# pass statement can be used with for loop in order not to leave the loop
# empty, the same as if-statement

for i in my_list:
    pass
