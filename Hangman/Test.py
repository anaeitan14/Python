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
    file = open(r"C:\Users\Eitan\Games\ok.txt", "r")

    text = file.read()
    print(text)
    file.close()