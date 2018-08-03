price = {}
price["banana"] = 4
price["apple"] = 2
price ["orange"] = 1.5
price["pear"] = 3
stock = {}
stock["banana"] = 6
stock["apple"] = 0
stock ["orange"] = 32
stock["pear"] = 15
total = 0
for gia in price:
    for luong in stock:
        if gia == luong:
            amount = price[gia]*stock[luong]
            print(gia)
            print("price: ", price[gia])
            print("stock: ",stock[luong])
            print("")
            total += amount
print("Total: ",total)
        