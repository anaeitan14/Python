def is_funny(string):
    return False not in [True if letter == 'a' or letter == 'h' else False for letter in string]


res = is_funny("haaaaahahahahhh")
print(res)