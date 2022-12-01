def show_hidden_word(secret_word, old_letters_guessed):
    letter_found = ""
    is_found = False
    for letter in secret_word:
        if letter in old_letters_guessed:
            letter_found += letter + " "
            is_found = True
        else:
            letter_found += " _ "
    return letter_found, is_found


word = "potato"

guess = ['t']

print(show_hidden_word(word, guess))