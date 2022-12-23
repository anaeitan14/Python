class BigThing:

    def __init__(self, name):
        self._name = name


    def size(self):
        return len(self._name)






class BigCat(BigThing):

    def __init__(self, name, weight):
        BigThing.__init__(self, name)
        self._weight = weight


    def size(self):
        if(self._weight> 20):
            return "Very Fat"
        elif(self._weight > 15):
            return "Fat"
        return "OK"



if __name__ == "__main__":
    cutie = BigCat("Eitan", 15)
    print(cutie.size())