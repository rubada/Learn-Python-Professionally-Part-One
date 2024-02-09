# Higher-order built-in functions
# As mentioned before these function can accept function as their arguments and
# or return function as an output.
# sorted()
# it is used to sort an iterable, (set, list, tuple, dictionary)
# Syntax:
# sorted(iterable, key, reverse)
# iterable set, list, tuple, dictionary.
# key a function that can be used and applied on the sort function
# reverse if True the iterable will be sorted in descending order
# False the iterable is sorted in ascending order.
my_dict = {"b": 4, "g": 9, "e": 2, "a": 7, "c": 1}
sort_dict = sorted(my_dict)

# This will return a list of dictionary keys
# print(sort_dict)

# To get the dictionary sorted
# print(my_dict.items())

# Sorting the dictionary by its keys
sort_dict1 = dict(sorted(my_dict.items()))
# print(sort_dict1)


# Sorting the dictionary by its values, using key parameter
# x is the subtuples inside the main list my_dict.items()
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

# sorting a list of tuples
list_tuples = [('b', 4), ('g', 9), ('e', 2), ('a', 7), ('c', 1)]
string_sort = sorted(list_tuples)
num_sort = sorted(list_tuples, key=lambda x: x[1])
# print(string_sort)
# print(num_sort)


# A user defined function can be used with sorted function
def even_num(x):
    return x % 2


numbers = [31, 10, 99, 56, 32, 87, 94, 3]
numbers_sort = sorted(numbers)
# numbers_sort_even = sorted(numbers, key=even_num)
numbers_sort_even = sorted(numbers, key=lambda x: x % 2)
numbers_sort_odd = sorted(numbers, key=lambda x: not x % 2)

# print(numbers_sort)

# The result is sorting the even numbers first then the odd number
# print(numbers_sort_even)
# print(numbers_sort_odd)

# To sort the even and odd numbers and then sort the even numbers first and
# then the odd number:
sort_even_odd = sorted(sorted(numbers), key=lambda x: x % 2)
# print(sort_even_odd)

sort_odd_even = sorted(sorted(numbers), key=lambda x: not x % 2)
# print(sort_odd_even)
