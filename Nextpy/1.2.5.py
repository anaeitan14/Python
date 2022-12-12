import functools

def function(num, item):
    print("Num is",num)
    print("Item is",item)
    print(num+1)
    return num + 1

password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
print(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")




