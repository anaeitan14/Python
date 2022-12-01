def prod_exist(shop):
    """Takes a list as an argument and prints a message accordingly if the item exists in the list or not"""
    product = input("Enter the product to search")
    if product in shop:
        print(product, " Exists")
    else:
        print(product, " Doesnt exist")


def prod_count(shop):
    """Takes a list as an argument and prints the amount of times an item repeats in the list"""
    product = input("Enter the product to count: ")
    print(shop.count(product))


def remove_item(shop):
    """Takes a list as an argument and removes the input item from the list"""
    product = input("Enter the product to remove: ")
    shop.remove(product.lower())
    print(product, " Removed")


def sort_alpha(shop):
    """Takes a list as an argument and sorts it alphabetically"""
    shop.sort()
    print("Sorted")


def illegal_prod(shop):
    """Takes a list as an argument and checks if it contains product that is considered illegal and prints it"""
    for product in shop:
        if not product.isalpha() or len(product) < 3:
            print(product + " is an illegal product")


def add_item(shop):
    """Receives a list as an argument and adds an item to it"""
    product = input("Enter the product to add: ")
    shop.append(product)
    print(product, " Added")


def total_delete(shop):
    """Deletes all the occurrences of an item in the list"""
    product = input("Enter the item to delete absolutely from the list: ")
    index = 0
    for item in shop[:]:
        if item == product:
            shop.remove(item)



def remove_duplicates():
    pass


def count(shop):
    pass
def sort_popularity(shop):
    pass


def ascii_sort(shop):
    pass


def menu(shopping_string):
    shopping_list = shopping_string.split(",")
    choice = 0

    while choice != 9:
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

        choice = int(input())

        match choice:
            case 1:
                print(shopping_list)
            case 2:
                print(len(shopping_list))
            case 3:
                prod_exist(shopping_list)
            case 4:
                prod_count(shopping_list)
            case 5:
                remove_item(shopping_list)
            case 6:
                add_item(shopping_list)
            case 7:
                sort_alpha(shopping_list)
            case 8:
                illegal_prod(shopping_list)
            case 9:
                break
            case 10:
                total_delete(shopping_list)
            case 11:
                remove_duplicates(shopping_list)
            case 12:
                sort_popularity(shopping_list)
            case 13:
                ascii_sort(shopping_list)
            case _:
                print("Invalid input")







def main():
    #shopping_string = input("Enter your shopping list: ")
    shopping_string = "Milk,Cottage,Potato,Potato,Teeth,table,computer,apple,Apple,cup"
    menu(shopping_string)




if __name__ == "__main__":
    main()


