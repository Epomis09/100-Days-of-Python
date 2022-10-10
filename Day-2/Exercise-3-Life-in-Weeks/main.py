# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nintyMonths = 90*12
nintyWeeks = 90*52
nintyDays = 90*365

monthsLeft = nintyMonths - int(age)*12
weeksLeft = nintyWeeks - int(age)*52
daysLeft = nintyDays - int(age)*365

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")