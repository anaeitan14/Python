def prod_exist(shopping_list):
    product = input("Enter the product to search")
    if product in shopping_list:
        print("Exists")
    else:
        print("Doesnt exist")


def illegal_prod(shopping_list):
    for product in shopping_list:
        if (not product.isalpha() or len(product) < 3):
            print(product + " is an illegal product")


def menu(shopping_string):
    shopping_list = shopping_string.split(",")
    choice = 0

    while choice != 9:
        print("""           
1) Show items
2) How many items?
3) Does the item exist in the list?
4) How many times does the item exist in the list?
5) Delete item
6) Add item
7) Sort alphabetically
8) Illegal items
9) Exit
        """)

        choice = int(input())

        match choice:
            case 1:
                print(shopping_string)
            case 2:
                print(len(shopping_list))
            case 3:
                prod_exist(shopping_list)
            case 4:
                product = input("Enter the product to count: ")
                print(shopping_list.count(product))
            case 5:
                product = input("Enter the product to remove: ")
                shopping_list.remove(product)
            case 6:
                product = input("Enter the product to add: ")
                shopping_list.append(product)
            case 7:
                shopping_list.sort()
                print("Sorted...")
            case 8:
                illegal_prod(shopping_list)
            case 9:
                return
            case _:
                print("Invalid input")







def main():
    shopping_string = input()
    menu(shopping_string)




if __name__ == "__main__":
    main()


