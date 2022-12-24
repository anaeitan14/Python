class UnderAge(Exception):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'You are under 18, you are currently {self.age}, you will be 18 in {18 - self.age} years'


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(name, age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


if __name__ == "__main__":
    send_invitation('Eitan',17)