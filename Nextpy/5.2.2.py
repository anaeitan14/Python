numbers = iter(list(range(1, 101)))

for i in numbers:
    print(i)
    next(numbers)
    next(numbers)

