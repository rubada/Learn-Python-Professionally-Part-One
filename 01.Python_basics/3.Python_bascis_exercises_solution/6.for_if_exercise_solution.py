# Question one
# Show the shape below, where the 0 is going to be " "(empty space),
# and the 1 is going to be "*" (astrisk sign).
# This will reveal an image!
shape = [
  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
]

# Solution 1
# define a new variable if the shape is to be stored and used later
Final_shape = ""
for row in shape:
    photo_part = ""
    for item in row:
        if item == 0:
            photo_part = f"{photo_part}  "
        elif item == 1:
            photo_part = f"{photo_part}* "
    # Add the each row (list) to the Final_shape variable with new line
    Final_shape = Final_shape + photo_part + "\n"
# print(Final_shape)


# Solution 2
# if the shape is to be printed directly
for row in shape:
    for item in row:
        if item == 0:
            # end default is \n another line, changing it to " "
            # it will print all items at the same line with space between
            # them
            print(" ", end=" ")
        else:
            print("*", end=" ")
    # Add a a line of spaces after each row (list)
    print(" ")


# Question two
# Given the following list, create one list that has two nested list one is
# even numbers the other is odd numbers, as shown below
# numbers = [22, 45, 62, 86, 93, 55, 72, 12, 13, 89]
# output: [[22, 62, 86, 72, 12], [45, 93, 55, 13, 89]]

numbers = [22, 45, 62, 86, 93, 55, 72, 12, 13, 89]
numbers_even_odd = []
for i in range(2):
    numbers_even_odd.append([])
    for num in numbers:
        if i == 0 and num % 2 == 0:
            numbers_even_odd[i].append(num)
        if i > 0 and num % 2 != 0:
            numbers_even_odd[i].append(num)

# print(numbers_even_odd)


# Question 3
# Update below code taking in account the following notes:
# 1. Print an error statement if the user input is not an integr
# 2. Remove the break statement when the user input is 0
# 3. The final list shouldn't contain 0

# Solution
list_numbers = []
n = 1
while n != 0:
    # eval() will check if the expression is a valid Python statement then it
    # will excuted.
    x = eval(input("Please enter an integer number:"))
    if isinstance(x, int):
        if x != 0:
            print("To break please enter 0")
        if x != 0:
            list_numbers.append(x)
    else:
        print("Error, the number should be an integer.")
    n = x

# print(list_numbers)
