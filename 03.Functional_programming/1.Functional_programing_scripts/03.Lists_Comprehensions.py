# List comprehension
# List comprehension is a concise (short) way to create a list from other list
# or lists using a "for" loop, it creates a clean code where the syntax is not
# complex.
# Using list comprehension will be faster than a conventional or standard for
# loop.
# Example

numbers = [22, 45, 62, 86, 93, 55, 72, 12, 13, 89]

# Create two list, one has even numbers other has odd numbers:
even_num_con = []
odd_num_con = []

for num in numbers:
    if num % 2 == 0:
        even_num_con.append(num)
    else:
        odd_num_con.append(num)

# print(even_num_con)
# print(odd_num_con)

# Another way is to use list comprehension
# The Syntax:
# new_list = [item for item in iterable if statement and/or else statement]
#                                     |
#                                     |
#                                    \ /
#                                 Expression
# expression any operation that is needed to be executed within the for loop
# item: is the item in the iterable
# iterable: is a list, set, dictionary, tuple, range, etc.
# if statement: its condition should return True.

even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 != 0]

# print(even_num)
# print(odd_num)

# if-else statement can be used in list comprehension:
numbers = [22, 45, 62, 86, 93, 55, 72, 12, 13, 89]

odd_even = ["even" if num % 2 == 0 else "odd" for num in numbers]

# print(odd_even)

# Nested list comprehension, let's say a list is needed as shown below
# [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

# To create such a list using "for" loop
my_list = []
for i in range(5):
    my_list.append([])
    for j in range(4):
        my_list[i].append(j)

# print(my_list)

# Using list comprehension:
my_list1 = [[j for j in range(4)] for i in range(5)]

# print(my_list1)

# If there is a nested list and it is required to be flattern:

numbers_list = [[22, 45, 62], [86, 93, 55, 72], [12, 13, 89]]
len_num = len(numbers_list)
numbers_flattern = [num for i in range(len_num) for num in numbers_list[i]]

# print(numbers_flattern)

# Sets and tuples can be created using list comprehension, instead of using
# [] use {} or tuple()
# Using tuple() instead of () because as discussed before the () can be used
# for line continuation
# Example
num_flat_tuple = tuple(num for i in range(len_num) for num in numbers_list[i])
num_flat_set = {num for i in range(len_num) for num in numbers_list[i]}
# print(num_flat_tuple)
# print(num_flat_set)

# List comprehension can be used with dictionaries to create new ones from
# old dictionaries or create a dictionary from two lists.

keys = ["name", "age", "country"]
values = [["John", "Henry", "Luca"],
          [22, 30, 15],
          ["USA", "UK", "Italy"]]

person_data = {keys[i]: values[i] for i in range(len(keys))}
# print(person_data)

# To use lambda with list comprehension as shown below
a = [1, 4, 5]
b = [3, 2, 9]

list_lambda = [(lambda x, y: x[i] + y[i])(a, b) for i in range(len(a))]

# print(list_lambda)

# Using lambda with list comprehension is a bit complicated, to write a
# readable clean use built-in function map, which will be discussed in
# part 4 in this section.
