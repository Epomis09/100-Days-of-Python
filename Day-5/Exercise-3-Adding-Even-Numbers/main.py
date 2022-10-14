#Write your code below this row 👇

sum_evens = 0
for number in range (1,101):
    if number % 2 == 0:
        sum_evens += number

print(sum_evens)