HANGMAN_ASCII_ART = """Welcome to the game Hangman\n 
			  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
print(HANGMAN_ASCII_ART)

MAXUS_TRIES = 6

HANGMAN_PHOTOS = {1:    """x-------x""",
2:  """x-------x
|
|
|
|
|""",
3:  """x-------x
|       |
|       0
|
|
|""",
4:  """x-------x
|       |
|       0
|       |
|
|""",
5:  """x-------x
|       |
|       0
|      /|\\
|
|""",
6:  """x-------x
|       |
|       0
|      /|\\
|      /
|""",
7:  """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

def check_valid_input(letter_guessed, old_letters_guessed):
    if not letter_guessed.isalpha() or len(letter_guessed) > 1:
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    return True



def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        letter_string = sorted(old_letters_guessed)
        print(" -> ".join(letter_string))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    letter_found = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            letter_found += letter + " "
        else:
            letter_found += " _ "
    return letter_found

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def main():
    letter = input("Guess a letter: ")
    old = ['a','b','c','p','l','e']
    word = "apple"

    print(check_valid_input(letter, old))
    try_update_letter_guessed(letter, old)
    print(show_hidden_word(word,old))
    print(check_win(word, old))

    word = input("Please enter a word:")
    print("_ " * len(word))
    print_hangman(4)


if __name__ == "__main__":
    main()

