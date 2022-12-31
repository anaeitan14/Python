import itertools


wallet = [20,20,20,10,10,10,10,10,5,5,1,1,1,1,1]

possible_count = 0

for option in range(1,16):
    options = itertools.combinations(wallet, option)
    for pos in set(options):
        if sum(pos) == 100:
            possible_count += 1

print(possible_count)