import random

words = ["monkey", "cat", "horse", "chicken", "elephant"]
word = random.choice(words)
print(word)

number_of_letter = len(word)
guess_word = []
for number in word:
    guess_word.append("_")
print(guess_word)

letter_input = input("Choose a word: ")

for letter in word:
    if letter == letter_input:
        print(word.index(letter))

