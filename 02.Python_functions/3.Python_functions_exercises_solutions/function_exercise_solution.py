# Question 1
# Write a function to count the number of uppercase and lowercase letters
# string: "Hello, my name is John. I am a Python Programmer, I want to become
# an experienced Python Programmer"
# output:
# Lower case letters = 71
# Upper case letters = 8

def lower_uppercase_count(my_string):
    lower_case = 0
    upper_case = 0
    for letter in my_string:
        if letter.islower():
            lower_case += 1
        elif letter.isupper():
            upper_case += 1
    return lower_case, upper_case


sent = "Hello, my name is John. I am a Python Programmer, I want to become\
    an experienced Python Programmer"
lower_case_letters, upper_case_letters = lower_uppercase_count(sent)
# print(f"Lower case letters {lower_case_letters}",
#       f"Upper case letters {upper_case_letters}",
#       sep="\n")


# Question 2
# Write a function to get the factorial number, which is the product of
# all positive integers less than or equal to a given positive integer.
# Example
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)


# print(factorial(6))


# Question 3
# Write a function to get Fibonacci numbers, which is he series of numbers
# where each number is the sum of the two preceding numbers.
# if x  = 10
# Solution 1 should equal = 55
# Solution 2 should be a list [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Solution 1 Recursion Function
def fibonacci(x):
    if x < 0:
        return "x shoukd be an integer larger than 0"
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


# print(fibonacci(10))


# Solution 2 return a list of fibonacci numbers
def fibonacci_nums(x):
    fibo = []
    n = 2
    fibo.append(0)
    fibo.append(1)
    fibo.append(1)
    while x != n:
        n = n + 1
        fibo.append(fibo[n-1] + fibo[n-2])
    return fibo


# print(fibonacci_nums(10))


# Question 4
# Write a function thar return the Greatest Common Divisor (GCD) of two
# numbers.
# GCD is the greatest number or factor that both numbers can be divided by.
# Example 4, 8, 16 their GCD is 4
# 4 factors are 1 2 4
# 8 factors are 1 2 4 8
# 16 factors are 1 2 4 8 16
# GCD is 4 because it can be divided by all three number.
# Check the GCD rules online.

def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


print(gcd(250, 300))
