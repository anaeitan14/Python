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

def choose_word(file_path, index):
    secret_words = open(file_path, "r")
    secret_words_list = []

    for line in secret_words:
        print(line)
        secret_words_list.append(line)

    print(type(secret_words_list))
    print(secret_words_list)

    count = 0

    for word in secret_words_list:
        if secret_words_list.count(word) != 1:
            count+=1

    if index >= len(secret_words_list):
        specialWord = secret_words_list[0]
    else:
        specialWord = secret_words_list[index-1]

    secret_words.close()

    return count, specialWord

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

    res = choose_word("words.txt", 2)
    print(res)

if __name__ == "__main__":
    main()

