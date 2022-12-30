def parse_ranges(ranges_string):
    number_range = (num.split("-") for num in ranges_string.split(","))

    all_nums = (num for one, two in number_range for num in range(int(one), int(two)+1))
    return all_nums






if __name__ == "__main__":
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))