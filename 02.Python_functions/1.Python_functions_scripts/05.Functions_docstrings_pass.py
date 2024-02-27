# Functions
# Docstrings can be passed inside the function, to describe the function task
# and define the parameters that are used in the function.
# The docstrings are optional, but using them will be a good practice to
# explain the function tasks.
# Example

def max_even_odd_num(my_sequnce):
    """This function returns the maximum even and odd numbers in a sequence.
    Parameters:
        my_sequence:
            A list, tuple, or set of integer numbers.
    Return:
            An integer number
    """
    even_nums = []
    odd_nums = []
    for number in my_sequnce:
        if number % 2 == 0:
            even_nums.append(number)
        else:
            odd_nums.append(number)
    return max(even_nums), max(odd_nums)


my_list = [2, 99, 65, 5, 82, 100, 283]
my_tuple = (3, 6, 7, 9, 8, 12, 16, 87)
my_set = {5, 6, 8, 2, 4, 9, 10, 3}

max_even_num, max_odd_num = max_even_odd_num(my_set)

# print(f"Even Maximum Number= {max_even_num}",
#       f"Odd Maximum Number= {max_odd_num}",
#       sep="\n")

# __doc__ dunder method can be used to print the docstrings of a function.
print(max_even_odd_num.__doc__)


# "pass" statement can be used, same as for while and if statements, in order
# not to leave the function empty.

def add():
    pass
