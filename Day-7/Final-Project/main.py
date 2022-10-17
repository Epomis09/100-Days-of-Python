import random

words = ["monkey", "cat", "horse", "chicken", "donkey"]
word = random.choice(words)
print(word)
number_of_letter = len(word)
guess_word = []
for number in word:
    guess_word.append("_")

# letter = input("Choose a word: ")
print(guess_word)
