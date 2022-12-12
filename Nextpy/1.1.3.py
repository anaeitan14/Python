def do_it(number):
    if number % 4 == 0:
        return True



def four_dividers(number):
    return list(filter(do_it,range(1,number+1)))





if __name__ == "__main__":
    print(four_dividers(9))
    print(four_dividers(3))