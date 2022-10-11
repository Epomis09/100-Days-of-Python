# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

mix_names = name1 + name2
names = mix_names.lower();

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
first_digit = t + r + u + e
l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
second_digit = l + o + v + e

result = int(str(first_digit) + str(second_digit))

if (result < 10) or (result > 90):
  print(f"Your score is {result}, you go together like coke and mentos.")
elif (result >= 40) and (result <= 50):
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")