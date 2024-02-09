# 1. Concatenating strings
a = "My name is"
b = "Ruba"
sent = a + " 3 " + b + " " + str(5)
# print(sent)

# 2. String formatting
# There are two ways to format the string
# 1. Using the format() method
year = "2023"
day = "24"
month = "May"
# There are different ways to use the format() method
sent1 = "I am taking this course in {} {}, {}.".format(month, day, year)
# print(sent1)

sent2 = "I am taking this course in {m} {d}, {y}!".format(m=month, d=day,
                                                          y=year)
# print(sent2)


sent3 = "I am taking this course in {0} {1}, {2}?".format(month, day, year)
# print(sent3)


sent4 = "I am taking this course in {1} {2}, {0}>".format(year, month, day)
# print(sent4)


# 3. Using Python f string, which is a new way to format strings, and it was
# introduced in Python version 3.6 and above.
sent5 = f"I am taking this course in {month} {day}, {year}"
print(sent5)
