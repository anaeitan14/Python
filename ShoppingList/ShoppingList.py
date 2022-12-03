def prod_exist(shop,product):
    """Takes a list as an argument and prints a message accordingly if the item exists in the list or not"""
    if product in shop:
        print(product, "exists in the list")
    else:
        print(product, "doesnt exist in the list")


def prod_count(shop,product):
    """Takes a list as an argument and prints the amount of times an item repeats in the list"""
    if product not in shop:
        print("Cannot count",product,"as it does not exist in the list")
        return
    print(product,"appears",shop.count(product),"times")


def remove_item(shop,product):
    """Takes a list as an argument and removes the input item from the list"""
    if product not in shop:
        print("Item cannot be removed because it does not exist in the list")
        return
    shop.remove(product)
    print(product, "was removed from the list")

def add_item(shop,product):
    """Receives a list as an argument and adds an item to it"""
    shop.append(product)
    print(product, " Added")

def sort_alpha(shop):
    """Takes a list as an argument and sorts it alphabetically"""
    shop.sort()
    print("Sorted")


def illegal_prod(shop):
    """Takes a list as an argument and checks if it contains product that is considered illegal and prints it"""
    illegal_exist = False
    for product in shop:
        if not product.isalpha() or len(product) < 3:
            print(product + " is an illegal product")
            illegal_exist = True
    if not illegal_exist:
        print("No illegal items were found")

def total_delete(shop,product):
    """Deletes all the occurrences of an item in the list"""
    if product not in shop:
        print("Cannot total delete item since it doesnt exist in the list")
        return
    while product in shop:
        shop.remove(product)

def remove_duplicates(shop,product):
    """Removes duplicate values from the list"""
    if product not in shop or shop.count(product) == 1:
        print("Cannot remove duplicates since product doesn't not exist or does not have duplicates")
        return

    while shop.count(product) != 1:
        shop.remove(product)

    print("Duplicates of",product,"removed")

def item_count(item):
    """Key function for sort parameter in sort_popularity function, returns the number of times an item appeared"""
    return item[-1]


def sort_popularity(shop):
    """Sorts based on the popularity of an item"""
    popular_list = []

    for item in shop:
        item_num = item+"-"+str(shop.count(item))
        popular_list.append(item_num)

    for item in popular_list:
        while popular_list.count(item) != 1:
            popular_list.remove(item)

    popular_list.sort(reverse=True, key=item_count)
    print(popular_list)


def ascii_func(item):
    """Key function for ascii_sort function, returns the sum of ascii values of an item"""
    total_sum = 0;
    for letter in item:
        total_sum += ord(letter)
    return total_sum

def ascii_sort(shop):
    """Sorts a list based on the ascii value of each item"""
    shop.sort(key=ascii_func)
    print("Sorted by ascii value")


def print_menu():
    """Prints the main menu"""
    print("""           
1) Show items
2) How many items are in the list?
3) Does the item exist in the list?
4) How many times does the item repeat in the list?
5) Delete item
6) Add item
7) Sort alphabetically
8) Print Illegal items
9) Exit
10) Total delete an item
11) Remove duplicates
12) Sort by popularity
13) Sort by ASCII value
            """)

def menu(shopping_string):
    shopping_list = shopping_string.lower().split(",")
    choice = 0

    while choice != 9:
        print_menu()
        choice = int(input())

        match choice:
            case 1:
                print(' '.join(shopping_list))
            case 2:
                print("There are", len(shopping_list), "items")
            case 3:
                product = input("Enter the product to search: ").lower()
                prod_exist(shopping_list,product)
            case 4:
                product = input("Enter the product to count: ").lower()
                prod_count(shopping_list,product)
            case 5:
                product = input("Enter the product to remove: ").lower()
                remove_item(shopping_list,product)
            case 6:
                product = input("Enter the product to add: ").lower()
                add_item(shopping_list,product)
            case 7:
                sort_alpha(shopping_list)
            case 8:
                illegal_prod(shopping_list)
            case 9:
                break
            case 10:
                product = input("Enter the item to delete absolutely from the list: ").lower()
                total_delete(shopping_list,product)
            case 11:
                product = input("Enter the product to remove duplicates from: ").lower()
                remove_duplicates(shopping_list,product)
            case 12:
                sort_popularity(shopping_list)
            case 13:
                ascii_sort(shopping_list)
            case _:
                print("Invalid input")


def main():
    shopping_string = input("Enter your shopping list: ")
    menu(shopping_string)




if __name__ == "__main__":
    main()


