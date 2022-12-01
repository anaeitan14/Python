def total_delete():
    shop = ["potato", "potato", "potato", "potato"]
    product = "potato"

    for grocery in shop[:]:
        if grocery == product:
            shop.remove(product)

    print(shop)




total_delete()
