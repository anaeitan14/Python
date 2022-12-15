def print_menu():
    """Prints the main menu"""
    print("""           
1) Show items
2) How many items are in the list?
3) Does the item exist in the list?
4) How many times does the item repeat in the list?
5) Delete item
6) Add item
8) Print Illegal items
9) Exit
10) Total delete an item
12) Sort by popularity
13) Sort by ASCII value
14) Total sum the items
15) Logout
16) Top 3 items
17) Search by pattern
            """)


def total_sum(shopping_dict):
    """Counts the total amount of items in the dictionary"""
    total = 0
    for count in shopping_dict.values():
        total += count
    print(total)


def ascii_func(item):
    """Helper function for sort_ascii, sums the ascii value of each word"""
    total_sum = 0
    for letter in item[0]:
        total_sum += ord(letter)
    return total_sum


def sort_ascii(shopping_dict):
    """Sorts by ascii value sum of each word"""
    print(sorted(shopping_dict.items(), key=ascii_func))


def popul_item(item):
    """Helper function for sort_popularity, returns the value of a key in a tuple"""
    return item[1]


def top_three_items(shopping_dict):
    """Returns the top 3 most frequent items by sorting a list and then slicing the first 3 elements"""
    sorted_list = sorted(shopping_dict.items(), key=popul_item, reverse=True)
    print("The top 3 most popular items are: ", (sorted_list[:3]))


def sort_popularity(shopping_dict):
    """Sorts by popularity of the value of each key using helper function popul_item"""
    print(sorted(shopping_dict.items(), key=popul_item, reverse=True))


def search_pattern(shopping_dict, pattern):
    """Searches by a given pattern by the user either contains a letter or starts with a pattern"""
    if pattern[0] == '*' and pattern[-1] == '*':
        for key, value in shopping_dict.items():
            if pattern[1:-1] in key:
                print(key, value)
    elif pattern[-1] == '*':
        for key, value in shopping_dict.items():
            if key.startswith(pattern[:-1]):
                print(key, value)


def total_delete(shopping_dict, product):
    """Totally deletes an item from the dictionary, checks if the item even exists in the dictionary beforehand"""
    if product not in shopping_dict.keys():
        print("Cannot total delete item as it does not exist in the list")
        return
    del shopping_dict[product]


def illegal_prod(shop_dict):
    """Checks if any of the items keys are illegal"""
    illegal_exist = False
    for key in shop_dict.keys():
        if not key.isalpha() or len(key) < 3:
            print(key + " is an illegal product")
            illegal_exist = True
    if not illegal_exist:
        print("No illegal items were found")


def add_prod(shop_dict, item):
    """Adds a product to the dictionary if the item already exists it increments its value otherwise starts it to 1"""
    if item not in shop_dict.keys():
        shop_dict[item] = 1
    else:
        shop_dict[item] += 1


def remove_prod(shop_dict, item):
    """Removes a product from the dictionary, checks beforehand if it even exists in the dictionary"""
    if item not in shop_dict.keys():
        print("Cant remove item as it does not exist")
        return
    elif shop_dict[item] > 1:
        shop_dict[item] -= 1
    else:
        del shop_dict[item]


def count_prod(shop_dict, item):
    """Counts how many times an item is in the dictionary"""
    if item not in shop_dict.keys():
        print("Cant count item as it does not exist")
        return
    count = shop_dict[item]
    print("The item appears",count,"times")


def search_prod(shop_dict, item):
    """Checks if an item exists in the dictionary"""
    if item in shop_dict.keys():
        print("Item exists")
    else:
        print("Doesn't exist")


def string_to_dict(shopping_string):
    """Takes the string, converts it into a list and then we scan the array and accordingly set values in our new dictionary"""
    shopping_list = shopping_string.lower().split(",")
    new_dict = {}

    for item in shopping_list:
        if item not in new_dict.keys():
            new_dict[item] = 1
        else:
            new_dict[item] += 1

    return new_dict


def menu(shopping_dict, users):
    """Main menu of the application"""
    choice = 0

    while choice != 9:
        print_menu()
        choice = int(input())

        match choice:
            case 1:
                print(shopping_dict)
            case 2:
                print(len(shopping_dict))
            case 3:
                product = input("Enter the product to search: ").lower()
                search_prod(shopping_dict, product)
            case 4:
                product = input("Enter the product to count: ").lower()
                count_prod(shopping_dict, product)
            case 5:
                product = input("Enter the product to remove: ").lower()
                remove_prod(shopping_dict, product)
            case 6:
                product = input("Enter the product to add: ").lower()
                add_prod(shopping_dict, product)
            case 8:
                illegal_prod(shopping_dict)
            case 9:
                break
            case 10:
                product = input("Enter the item to delete absolutely from the list: ").lower()
                total_delete(shopping_dict, product)
            case 12:
                sort_popularity(shopping_dict)
            case 13:
                sort_ascii(shopping_dict)
            case 14:
                total_sum(shopping_dict)
            case 15:
                print("Logout")
                print(users)
                multi_user(users)
            case 16:
                top_three_items(shopping_dict)
            case 17:
                pattern = input("Enter a pattern to search by: ")
                search_pattern(shopping_dict, pattern)
            case _:
                print("Invalid input")


def multi_user(users):
    """User management function, takes in the dictionary containing all the users and their inner dictionaries,
    checks if username already exists if not makes it a new key"""
    #"Potato,chips,cola,potato,table,table,Water,Water,potato,cola,cola,cola,cola,cola,cola,cola"

    print("Login")
    username = input("Enter your username: ")
    if username in users.keys():
        menu(users[username], users)
    else:
        users[username] = string_to_dict(input("Enter your shopping list: "))
        menu(users[username], users)


def main():
    users = {}
    multi_user(users)


if __name__ == "__main__":
    main()
