#Write your code below this row 👇

fizz = 'Fizz'
buzz = 'Buzz'

for number in range (1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print(fizz+buzz)
    elif number % 3 == 0:
        print(fizz)
    elif number % 5 == 0:
        print(buzz)
    else:
        print(number)
        # print(f"{number}\n")