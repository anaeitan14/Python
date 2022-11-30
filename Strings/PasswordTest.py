def repeat_words(password, name):
    if(password.startswith("password") or password.endswith("password")):
        return 0
    elif(name in password):
        return 3
    elif("1234" in password or "abc" in password or "ABC" in password):
        return 5
    elif("love" in password):
        return 7
    return 10



def check_length(password):
    length = len(password)

    if(length < 5):
        return 0
    elif(length < 8):
        return 3
    elif(length < 10):
        return 6
    else:
        return 10


def char_variety(password):
    if(password.isdigit()):
        return 0
    elif(password.islower() or password.isupper()):
        return 3
    elif(password.isalpha()):
        return 5
    elif(password.isalnum()):
        return 7
    else:
        return 10

def calculate_grade(length_grade, char_grade, repeated_grade):
    sum = length_grade + char_grade + repeated_grade
    avg = sum/3
    if(avg < 3):
        return "very weak"
    elif(avg < 5):
        return "medium"
    elif(avg < 7):
        return "medium"
    elif(avg < 9):
        return "strong"
    else:
        return "very strong"

def check_password(password, name):
    length_grade = check_length(password)
    char_grade = char_variety(password)
    repeated_grade = repeat_words(password, name)
    grade = calculate_grade(length_grade, char_grade, repeated_grade)
    return grade


def main():
    name = input("Enter your name")
    password = input("Enter your password")
    grade = check_password(name, password)
    print(grade)
main()