def price_tuple(tuple):
    return tuple[0][1]

def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, reverse=True, key=price_tuple)



if __name__ == "__main__":
    items = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    res = sort_prices(items)
    print(res)