# question one
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


# question two
# Given the following list, create one list that has two nested list one is
# even numbers the other is odd numbers, as shown below
# numbers = [22, 45, 62, 86, 93, 55, 72, 12, 13, 89]
# output: [[22, 62, 86, 72, 12], [45, 93, 55, 13, 89]]


# question 3
# Update below code taking in account the following notes:
# 1. Print an error statement if the user input is not an integr
# 2. Remove the break statement when the user input is 0
# 3. The final list shouldn't contain 0

list_numbers = []
n = 1
while n != 0:
    x = int(input("Please enter an integer number:"))
    print("To break please enter 0")
    list_numbers.append(x)
    n = x
