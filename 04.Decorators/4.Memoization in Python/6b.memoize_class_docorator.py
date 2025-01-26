# Memoization in Python:

# When calling the function using "MemoizeDec",
# if the key is not stored in the dictionary
# (self.memory_dict), then the result will be
# calculated by the function and then will be
# stored in the dictionary (self.memory_dict).
# If the values exist in the dictionary
# (self.memory_dict), then the result
# will be taken from the dictionary
# (self.memory_dict), which will speed up
# the code executing.

class MemoizeDec:

    def __init__(self, func):
        self.func = func
        # Define an empty dictionary:
        self.memory_dict = {}

    def __call__(self, *args, **kwargs):
        # Store the argument in a tuple to use them
        # as dictionary keys.
        key = (*args, *kwargs.items())

        if key in self.memory_dict:
            print("Getting the result stored in the\
memoization decorator dictionary:")
            return self.memory_dict[key]

        result = self.func(*args, **kwargs)
        self.memory_dict[key] = result

        return result


@MemoizeDec
def add(x, y):
    print("The sum of two numbers using add() function")
    return x + y


print(add(2, 3))
print(add(5, 6))

print(add(2, 3))
print(add(5, 6))
