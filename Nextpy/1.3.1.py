def intersection(list_1, list_2):
    return list(set([num1 for num1 in list_1 for num2 in list_2 if num1 == num2]))


print(intersection([5,5,6,6,7,7], [1,5,9,5,6]))