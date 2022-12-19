import functools
def one():
    with open("names.txt", "r") as file_obj:
        print(max(file_obj.readlines()))

def two():
    with open("names.txt", "r") as file_obj:
        print(sum([len(word[:-1]) for word in file_obj]))

def three():
    with open("names.txt", "r") as file_obj:
        print("".join(sorted(file_obj.readlines(), key=lambda word: len(word))[:2]))


def four():
    with open("names.txt", "r") as file_obj, open("name_length.txt", "w") as write_obj:
        length = [str(len(word[:-1])) for word in file_obj.readlines()]
        write_obj.write("\n".join(length))

def five():
    name_length = int(input("Enter name length: "))
    with open("names.txt", "r") as file_obj:
        print("".join([name for name in file_obj.readlines() if len(name[:-1]) == name_length]))


if __name__ == "__main__":
    five()
