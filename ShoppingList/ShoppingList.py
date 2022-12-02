def prod_exist(shop,product):
    """Takes a list as an argument and prints a message accordingly if the item exists in the list or not"""
    if product in shop:
        print(product, "exists in the list")
    else:
        print(product, "doesnt exist in the list")


def prod_count(shop,product):
    """Takes a list as an argument and prints the amount of times an item repeats in the list"""
    if product not in shop:
        print("Cannot print product because it doesnt exist in the list")
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
    for product in shop:
        if not product.isalpha() or len(product) < 3:
            print(product + " is an illegal product")

def total_delete(shop,product):
    """Deletes all the occurrences of an item in the list"""
    if not prod_exist(shop,product):
        print("Cannot total delete item since it doesnt exist in the list")
        return
    for item in shop[:]:
        if item == product:
            shop.remove(item)


def remove_duplicates(shop,product):
    """Removes duplicate values from the list"""
    if not prod_exist(shop,product) or prod_count(shop,product) == 1:
        print("Cannot remove duplicates since product doesn't not exist or does not have duplicates")
        return

    shop.remove(product)
    print("Duplicates of",product,"removed")


def count(shop):
    pass


def item_count(item):
    """Key function for sort parameter in sort_popularity function, returns the number of times an item appeared"""
    return item[-1]
def sort_popularity(shop):
    """Sorts based on the popularity of an item"""
    popular_list = []

    for item in shop:
        item_num = item+"-"+str(shop.count(item))
        popular_list.append(item_num)

    for item in popular_list[:]:
        if popular_list.count(item) > 1:
            popular_list.remove(item)


    popular_list.sort(reverse=True, key=item_count)
    print(popular_list)



def ascii_sort(shop):
    pass


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
                print(shopping_list)
            case 2:
                print("There are", len(shopping_list), "items")
            case 3:
                product = input("Enter the product to search: ")
                prod_exist(shopping_list,product)
            case 4:
                product = input("Enter the product to count: ")
                prod_count(shopping_list,product)
            case 5:
                product = input("Enter the product to remove: ")
                remove_item(shopping_list,product)
            case 6:
                product = input("Enter the product to add: ")
                add_item(shopping_list,product)
            case 7:
                sort_alpha(shopping_list)
            case 8:
                illegal_prod(shopping_list)
            case 9:
                break
            case 10:
                product = input("Enter the item to delete absolutely from the list: ")
                total_delete(shopping_list,product)
            case 11:
                product = input("Enter the product to remove duplicates from: ")
                remove_duplicates(shopping_list,product)
            case 12:
                sort_popularity(shopping_list)
            case 13:
                ascii_sort(shopping_list)
            case _:
                print("Invalid input")
                input("Press enter to go back to the mnu")

def main():
    #shopping_string = input("Enter your shopping list: ")
    shopping_string = "Milk,Milk,Milk,Milk,Milk,Cottage,Potato,Potato,Teeth,table,table,table,table,table,table,table,table,computer,apple,Apple,cup"
    menu(shopping_string)




if __name__ == "__main__":
    main()


