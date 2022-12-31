class IDIterator:
    def __init__(self, id):
        self.id = id

    def __iter__(self):
        return self

    def __next__(self):
        if self.id < 1000000000:
            self.id = self.id + 1
            while not check_id_valid(self.id):
                self.id = self.id + 1
            return self.id
        else:
            raise StopIteration

def check_id_valid(id_number):
    total_sum = 0
    id_string = str(id_number)
    for num in id_string:
        if len(id_string) % 2 == 0:
            total_sum+= (int(num)*2)%10 + (int(num)*2)//10
        else:
            total_sum+=int(num)
        id_string = id_string[:-1]

    if total_sum % 10 == 0:
        return True
    return False


if __name__ == "__main__":
    id = int(input("Enter ID: "))
    iterate_id = IDIterator(id)

    for i in range(10):
        print(next(iterate_id))
