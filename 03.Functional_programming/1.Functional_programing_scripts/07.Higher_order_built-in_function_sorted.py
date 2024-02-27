# Higher-order built-in functions
# As mentioned before these functions can accept a function or functions as
# their arguments and/or return a function or functions as an output.
# sorted()
# it is used to sort an iterable, (set, list, tuple, dictionary).
# Syntax:
# sorted(iterable, key, reverse)
# iterable: such as set, list, tuple, dictionary.
# Key: is a function that can be used and applied to the sort function
# Reverse: if True the iterable will be sorted in descending order, False
# which is the default value the iterable is sorted in ascending order.

my_dict = {"b": 4, "g": 9, "e": 2, "a": 7, "c": 1}
sort_dict = sorted(my_dict)

# This will return a list of the dictionary keys:
# print(sort_dict)

# To sort a dictionary, use the items() method:
# print(my_dict.items())

# Then sorting the dictionary by its keys:
sort_dict1 = dict(sorted(my_dict.items()))
# print(sort_dict1)


# Or sorting the dictionary by its values, using the key parameter
# of the sorted() function.
# The x variable, of the lambda function, is the subtuple inside the main
# list my_dict.items(), and x[1] is the 2nd item in the subtuple, which is
# the dictionary value.
sort_dict2 = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# print(sort_dict2)

# Another Example
personal_data = [
    {'name': 'John', 'age': 22, 'country': 'USA'},
    {'name': 'Mary', 'age': 30, 'country': 'UK'},
    {'name': 'Luca', 'age': 15, 'country': 'Italy'},
    {'name': 'Mohammad', 'age': 34, 'country': 'Eygpt'},
    {'name': 'Leen', 'age': 25, 'country': 'Jordan'},
    ]

# personal_data is a list of dictionary, x are the dictionaries in this list
age_sort = sorted(personal_data, key=lambda x: x["age"], reverse=True)
# print(age_sort)

# Sorting a list of tuples
list_tuples = [('b', 4), ('g', 9), ('e', 2), ('a', 7), ('c', 1)]
string_sort = sorted(list_tuples)
num_sort = sorted(list_tuples, key=lambda x: x[1])
# print(string_sort)
# print(num_sort)


# A user-defined function can be used with sorted() function:
def even_num(x):
    return x % 2


numbers = [31, 10, 99, 56, 32, 87, 94, 3]
numbers_sort = sorted(numbers)
# numbers_sort_even = sorted(numbers, key=even_num)
numbers_sort_even = sorted(numbers, key=lambda x: x % 2)
numbers_sort_odd = sorted(numbers, key=lambda x: not x % 2)

# print(numbers_sort)

# The result is sorting the even numbers first then the odd numbers:
# print(numbers_sort_even)
# print(numbers_sort_odd)

# To sort the even and odd numbers and then sort the even numbers first and
# then the odd numbers:
sort_even_odd = sorted(sorted(numbers), key=lambda x: x % 2)
# print(sort_even_odd)

sort_odd_even = sorted(sorted(numbers), key=lambda x: not x % 2)
# print(sort_odd_even)
