# Let's take the following example
# When calling the function using memoize_dec, if the key is not stored
# in the memory_func dictionary, then the result will be calculated by function
# and then will be stored in the dictinary.
# If the values does exist in the memory_func, then the result will be taken
# from the memory_func, which will reduce the time of the code excuting.
# Check online to read more about memoize decorator.
def memoize_dec(func):
    memory_func = {}

    def wrapper(*args, **kwargs):
        # Store the argument in a tuple to use them as keys in a dictionary
        key = (*args, *kwargs.items())

        if key in memory_func:
            print("Getting the result from memory_func:")
            return memory_func[key]

        result = func(*args, **kwargs)
        memory_func[key] = result

        return result

    return wrapper


@memoize_dec
def add(x, y):
    print("Calculating the sum of two numbers using function add()")
    return x + y


print(add(2, 3))
print(add(5, 6))

print(add(2, 3))
print(add(5, 6))
