import random


def print_start():
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


def print_hangman(num_of_tries, HANGMAN_PHOTOS):
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
    is_found = False
    for letter in secret_word:
        if letter in old_letters_guessed:
            letter_found += letter + " "
            is_found = True
        else:
            letter_found += " _ "
    return letter_found, is_found

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def choose_word(file_path, index):
    secret_words = open(file_path, "r")

    words = secret_words.read().split(" ")
    print(words)

    count = 0

    for word in words:
        if words.count(word) == 1:
            count += 1

    if index >= len(words):
        index = index - len(words)

    secret_words.close()

    return count, words[index-1]
def main():
    game_loop()


def game_loop():
    HANGMAN_PHOTOS = {1: """x-------x""",
                      2: """x-------x
|
|
|
|
|""",
              3: """x-------x
|       |
|       0
|
|
|""",
              4: """x-------x
|       |
|       0
|       |
|
|""",
              5: """x-------x
|       |
|       0
|      /|\\
|
|""",
              6: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
              7: """x-------x
|       |
|       0
|      /|\\
|      / \\
      |"""}

    MAXUS_TRIES = 7
    num_of_tries = 0
    old_letters_guessed = []
    secret_word = choose_word("words.txt", random.randint(1,5))[1]
    current_guess = ""
    print_start()

    while num_of_tries < MAXUS_TRIES:
        user_letter = input("Guess a letter: ")
        try_update_letter_guessed(user_letter, old_letters_guessed)
        current_guess = (show_hidden_word(secret_word, old_letters_guessed))
        print(current_guess[0])

        if not current_guess[1]:
            print(current_guess[1])
            num_of_tries += 1

        if check_win(secret_word, old_letters_guessed):
            print("You won!!!")
        else:
            print_hangman(num_of_tries+1, HANGMAN_PHOTOS)

    print("You lost... :(")


if __name__ == "__main__":
    main()
