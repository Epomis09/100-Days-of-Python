import random
from stages import stages, logo
from hangman_words import word_list

lives = 6
flag = True
guess_word_list = []
word = random.choice(word_list)
print(logo)
print(word)

def list_to_string():
    guess_word = ' '.join(guess_word_list)
    print(f"Your guess word is: {guess_word}")
    
for number in word:
    guess_word_list += "_"

while(flag):
    list_to_string()
    print(stages[lives])
    letter_input = input("Choose a word: ").lower()
    if letter_input in guess_word_list:
        print(f"You entered '{letter_input}' already!")
    if letter_input not in word:
        print(f"You guessed '{letter_input}', that's not in the word. You lose a life.")
        lives -= 1
    for (index, letter) in enumerate(word):
        if letter == letter_input:
            guess_word_list[index] = letter
        # print(word.index(index))  //in this way index return first item in list

        if lives == 0:
            list_to_string()
            print(stages[lives])
            print(f"You lose! Game Over!!! Your guess word was '{word}'!")
            flag = False
            break
        elif ("_" in guess_word_list) == False:
            list_to_string()
            print(f"You win! Congratulations!!! You found '{word}' word!")
            flag = False
            break
