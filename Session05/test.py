# quy = ["Quý", 20, "Vĩnh Phúc", 2, 3, ["Anime","ping pong"]]
# dictionary
# CRUD: Create, Read, Update, Delete
# key : value

# Create
person = {
    "name": "Quý",
    "age": 20,
    "university": "hust",
    "ex": 2,
    "fav": ["Anime","Ping Pong"]
}
# key = "fav"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

# Vòng lặp loại 1
# for key in person.keys():
#     print(key, end ="\t")

# Vòng lặp loại 2
# for key, value in person.items():
#     print(key, value, sep = ": ")

# Vòng lặp loại
# for value in person.values():
#     print(value)

# Update

# Thêm mới cặp key/ values
# person["gender"] = "male"
# print(person)

# Sửa cặp key/value
# person["ex"] = 20
# print(person)

# Delete

# del person["age"]
# print(person)
print(key)