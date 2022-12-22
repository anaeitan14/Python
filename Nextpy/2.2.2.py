class Bear:
    count_animals = 0
    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age
        Bear.count_animals += 1


    def birthday(self):
        self._age+=1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name




if __name__ == "__main__":
    animal_one = Bear(55, "Beary")
    animal_two=Bear(3)

    print(animal_two.get_name())
    print(animal_one.get_name())

    animal_one.set_name("Okay")
    print(animal_one.get_name())
    print(Bear.count_animals)