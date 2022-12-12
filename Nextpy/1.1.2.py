def do_it(letter):
    return letter*2


def double_letter(my_str):
    return "".join(list(map(do_it,my_str)))





if __name__ == "__main__":
    print(double_letter("python"))
    print(double_letter("we are the champions!"))