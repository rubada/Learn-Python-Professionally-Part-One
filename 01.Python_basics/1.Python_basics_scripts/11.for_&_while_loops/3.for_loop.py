# Nested for loop
# for i in range(1, 3):
#     print("outer loop", i)
#     for j in range(2):
#         print("inner loop", i, j)

# Another example
num1 = [1, 3, 4]
num2 = [3, 4, 6, 8]

for i in num1:
    print(f"Number {i}")
    for j in num2:
        add = f"{i} + {j} = {i + j}"
        print(add)

# Nested loops have advantages and disadvantages, you can check them by
# yourself, but the most important disadvantage is when using many nesting
# loops, then it will be difficult to understand, and they consume more memory
# when used with large data.
