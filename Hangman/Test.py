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

def check_increment_try(secret_word, user_letter):
    if user_letter in secret_word:
        return True
    return False



if __name__ == "__main__":

    user_letter = "t"
    secret_word = "tank"
    num_of_tries = 0

    if not check_increment_try(secret_word, user_letter):  # if the letter doesn't appear in the secret word, increment the amount of guesses and change the hangman picture to print
        num_of_tries += 1

    print(num_of_tries)
