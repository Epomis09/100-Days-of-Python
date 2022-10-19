import random

# words = ["monkey", "cat", "horse", "chicken", "elephant"]
words = [ "dog", "cat"]
game_over_counter = 6
flag = True
guess_word = []
word = random.choice(words)
print(word)

for number in word:
    guess_word.append("_")

while(flag):
    print(guess_word, game_over_counter)
    letter_input = input("Choose a word: ").lower()
    if letter_input in guess_word:
        print(f"You entered '{letter_input}' already!")
    if letter_input not in word:
        game_over_counter -= 1
    for (index, letter) in enumerate(word):
        if letter == letter_input:
            guess_word[index] = letter
        # print(word.index(index))  //in this way index return first item in list

        if game_over_counter == 0:
            print(f"You lose! Game Over!!! Your guess word was '{word}'!")
            flag = False
            break
        elif ("_" in guess_word) == False:
            print(f"You win! Congratulations!!! You found '{word}' word!")
            flag = False
            break
