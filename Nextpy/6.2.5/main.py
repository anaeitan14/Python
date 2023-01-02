from file2 import BirthdayCard
from file1 import GreetingCard

def main():

    greeting = GreetingCard()
    birthday = BirthdayCard()

    greeting.greeting_msg()
    birthday.greeting_msg()



if __name__ == "__main__":
    main()