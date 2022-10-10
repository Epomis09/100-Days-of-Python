# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Wrong Way!
# new_two_digit_number = int(two_digit_number)
# print(two_digit_number[0]+two_digit_number[1])

print(int(two_digit_number[0])+int(two_digit_number[1]))

# Advanced Way!
# print(sum(int (i) for i in two_digit_number))