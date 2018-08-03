inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# Thêm key pocket
inventory["pocket"]=["seashell","strang","berry","lint"]
print(inventory)
# Loại bỏ dagger khỏi backpack
inventory["backpack"].remove("dagger")
print(inventory)
# Thêm 50 vào gold
inventory["gold"] += 50
print(inventory)

