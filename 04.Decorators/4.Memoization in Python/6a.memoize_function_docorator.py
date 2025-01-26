# Memoization in Python:

# When calling the function using memoize_dec,
# if the key is not stored in the dictionary
# (memory_dict), then the result will be calculated
# by the function and then will be stored in the
# dictionary (memory_dict).
# If the values exist in the dictionary (memory_dict),
# then the result will be taken from the dictionary
# (memory_dict), which will speed up the code
# executing.

def memoize_dec(func):
    # Define an empty dictionary:
    memory_dict = {}

    def wrapper(*args, **kwargs):
        # Store the argument in a tuple to use them as
        # dictionary keys.
        key = (*args, *kwargs.items())

        if key in memory_dict:
            print("Getting the result stored in the\
memoization decorator dictionary:")
            return memory_dict[key]

        result = func(*args, **kwargs)
        memory_dict[key] = result

        return result

    return wrapper


@memoize_dec
def add(x, y):
    print("The sum of two numbers using add() function")
    return x + y


print(add(2, 3))
print(add(5, 6))

print(add(2, 3))
print(add(5, 6))
