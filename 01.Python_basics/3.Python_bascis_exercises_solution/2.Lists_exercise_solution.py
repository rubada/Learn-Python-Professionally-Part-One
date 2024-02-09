# 1st question:
# Use input() function to write a code asking
# for recovery email: such as john.smith@email.com
# and then print the output as shown below:
# "Your recovery email is: jo********@email.com

email = input("Enter recovery email:")
email_list = email.split("@")

visable_part = email_list[0][:2]

hidden_part_lenght = len(email_list[0][2:])
hidden_part = hidden_part_lenght * "*"
recovery_email = ("Your recovery email is: "
                  f"{visable_part}{hidden_part}@{email_list[1]}")

print(recovery_email)


# In the following exercises try to guess the output before
# running the code

new_list = [3, 6, "green", 9.5, "apple", ["red", True, "banana"],
            "banana", False, "orange", "banana"]

# 2nd question:
# What is the output of the following:

a = new_list[6::-3]

b = new_list[5][-3:-1]

c = new_list[-6:-1:4]

d = new_list[5:7]

# 3rd question
# Guess the final list after applying the following methods?
new_list.remove("banana")
new_list.pop()
new_list.pop(3)
new_list.append("blue")
new_list.sort(reverse=True)
new_list.extend([4, 7.8])
new_list.insert(2, 5)
