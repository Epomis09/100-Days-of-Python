alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift_word = ''

while True:
    while True:
        crypt = input("Type 'en' for encode or type 'de' for decode: ").lower()
        if (crypt != 'en') and (crypt != 'de'):
            print("Your input not valid!")
        else:
            break
    text = input("Enter Your Text: ").lower()
    shift = int(input("Enter Number you want to shift: "))

    def crypting(text, shift, crypt):
        global shift_word
        for letter in text:
            if letter not in alphabet:
                shift_word += letter
                continue
            letter_index = alphabet.index(letter)
            encrypt_index = letter_index + shift
            decrypt_index = letter_index - shift
            if crypt == "en":
                if encrypt_index > 25:
                    encrypt_index = (encrypt_index % 25) - 1
                shift_word += alphabet[encrypt_index]
            elif crypt == "de":
                if decrypt_index < 0:
                    decrypt_index = (decrypt_index % 25) + 1
                shift_word += alphabet[decrypt_index]
        print(shift_word)

    crypting(text, shift, crypt)
    shift_word = ''
    again_input = input("Do you want Encode or Decode again? Type 'y' for another one or press a key for exit! ")
    if again_input == 'y':
        print("-------------------")
        continue
    else:
        print("Bye bye!")
        break