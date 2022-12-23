class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def get_name(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0


    def feed(self):
        self.hunger-=1

    def __str__(self):
        return "Animal"

    def talk(self):
        pass




class Dog(Animal):
    def __str__(self):
        return "Dog"
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def __str__(self):
        return "Cat"
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self,name,hunger,stink_count=6):
        Animal.__init__(self,name,hunger)
        self.stink_count = stink_count

    def __str__(self):
        return "Skunk"
    def talk(self):
        print("tssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __str__(self):
        return "Unicorn"
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("Im not your toy...")


class Dragon(Animal):

    def __init__(self,name,hunger, color="Green"):
        Animal.__init__(self,name,hunger)
        self.color = color
    def __str__(self):
        return "Dragon"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

if __name__ == "__main__":
    d = Dog("Brownie", 10)
    c = Cat("Zelda", 3)
    s = Skunk("Stinky", 0)
    u = Unicorn("Keith", 7)
    dr = Dragon("Lizzy", 1450)

    zoo_lst = [d,c,s,u,dr]


    dog = Dog("Doggo", 80)
    cat = Cat("Kitty", 80)
    skunk = Skunk("Stinky Jr.", 80)
    unicorn = Unicorn("Clair", 80)
    dragon = Dragon("McFly", 80)

    zoo_lst.append(dog)
    zoo_lst.append(cat)
    zoo_lst.append(skunk)
    zoo_lst.append(unicorn)
    zoo_lst.append(dragon)


    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal ,animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)

