def is_funny(string):
    [False if char != 'h' else True for char in string]

print(is_funny("hahahahahaha"))