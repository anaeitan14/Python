def count_chars(my_str):
    magic_dict = {}

    for letter in my_str:
        magic_dict[letter[0]] = my_str.count(letter)

    return magic_dict




magic_str = "abra cadabra"
di_res = count_chars(magic_str)
print(di_res)
print(type(di_res))