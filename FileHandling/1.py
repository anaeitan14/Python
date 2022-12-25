def one(file_name, index):
    f = open(file_name, "r")
    words = f.read().split()

    if len(words) <= index:
        print("Index is bigger then amount of words")
        return
    print(words[index])

    f.close()

if __name__ == "__main__":
    one("test.txt", 2)