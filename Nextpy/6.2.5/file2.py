from file1 import GreetingCard



class BirthdayCard(GreetingCard):
    def __init__(self):
        super().__init__()
        self.sender_age = 0


    def greeting_msg(self):
        print("Recipient is", self.recipient, "sender is",self.sender, "Happy birthday,",self.sender_age, "years old!")





