import functools

# 1st Question
# Find the words that don't contain vowels in the below List the vowels list
# vowels = ["a", "e", "i", "o", "u"]
list_words = ["name",  "dry", "love", "cry", "run", "crypt", "Age", "Gym",
              "End", "Myth"]
# output:
# ['dry', 'cry', 'crypt', 'Gym', 'Myth']


# Solution
def check_vowels(letter):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if letter in vowels:
        return False
    else:
        return True


non_vowels_words = list(
    filter(
        lambda word: (all(check_vowels(i) for i in word)),
        list_words)
        )
# print(non_vowels_words)


# Explanation
# The lambda function is equal to the following function:
def words(word):
    # all() function returns True if all the return values from check_vowels()
    # True, let's take the word "hello"
    # check_vowels return (F, T, F, F, T) after using list comprehension, then
    # the all() will return False thus the word will not be included,
    # Another example "dry word", check_vowels return (T, T, T) then all() will
    # return True

    if all(check_vowels(i) for i in word):
        return word


# Another solution using the words function
non_vowels_words1 = list(filter(words, list_words))
# print(non_vowels_words1)


# 2nd Question
# Get the square root and cubic root of the following list, round them to
# 2 digits, and store them in a dictionary.

numbers = [300, 456, 678, 899, 275, 358]
# output:
# {
# 300: [17.32, 6.69],
# 456: [21.35, 7.7],
# 678: [26.04, 8.79],
# 899: [29.98, 9.65],
# 275: [16.58, 6.5],
# 358: [18.92, 7.1]
# }


def sqr_root(num): return num**(1/2)


def cubic_root(num): return num**(1/3)


funcs = [sqr_root, cubic_root]
round_digit = [2] * len(numbers)

roots_num = [list(             # using list() and map() to create a list of
    map(                       # sqr_num and cubic_num
        lambda func: func(num), funcs))
        for num in numbers]    # create the outer list using list comprehension

roots_num = list(
    map(
        lambda list_root: [round(num, 2) for num in list_root],
        roots_num)
        )

root_num_dict = dict(zip(numbers, roots_num))
# print(root_num_dict)


# 3rd Question
# Use the keys in dict_one and values in dict_two to create a new dictionary
# using the above keys and values
dict_one = {"Color": "Red", "Vegetable": "Tomato", "Fruit": "Apple"}
dict_two = {"A": "Orange", "B": "Pumpkin", "C": "Orange"}

# Output = {'Color': 'Orange', 'Vegetable': 'Pumpkin', 'Fruit': 'Orange'}

dict_new = dict(zip(dict_one, dict_two.values()))

# print(dict_new)

# 4th Question
# Use the reduce() to change a nested list into one list.
nest_list = [
    [1, 2, 3],
    [44, 65, 76, 89],
    [33, 90, 10, 43, 88],
    [5, 7, 9]
    ]

# Output = [1, 2, 3, 44, 65, 76, 89, 33, 90, 10, 43, 88, 5, 7, 9]

new_list = functools.reduce(list.__add__, nest_list)
# print(new_list)

# 5th Question
# Find the intersections in the following list, using reduce()
nest_list1 = [[89, 1, 2, 3, 44], [44, 65, 76, 89, 2], [2, 33, 90, 10, 44, 89]]

# First change the sublists into sets using map() function on nest_list
# no need to use a list() with a map(), it can be kept as an object.
# Note that all the sublists should have the same intersection item
# otherwise, the item will not be returned. You check it and remove one of the
# intersection items.
# Then use reduce() with the set intersection method to find the intersection.

inter_nums = functools.reduce(set.intersection, map(set, nest_list1))
# print(inter_nums)

# 6th Question
# Sort the following list according to the string length in descending order.

colors = ["red", "green", "black", "yellow", "purple", "grey", "magenta"]

# solution
colors_len = sorted(colors, key=len, reverse=True)
# print(colors_len)


# 7th Question
# Sort the following list according to the last letter in the string in
# descending order.

colors = ["red", "green", "black", "yellow", "purple", "grey", "magenta"]

# solution
colors_last = sorted(colors, key=lambda x: x[-1], reverse=True)
# print(colors_last)
