# list:
# CRUD
    # Create
    # Read
    # Update
    # Delete
menu = ["Cơm","Cá","Thịt bò","Ghẹ","Pizza","Gà ở Trần Duy Hưng"]
# Separator
# Length
# 1.
for i in range(len(menu)):
    print(menu[i])
# 2.1
for index, item in enumerate(menu,1):
    print(index, item,sep=". ")
# 2.2: index và items chỉ là 2 biến số, có thể thay thế bằng biến khác
# Key là enumerate
for index, item in enumerate(menu):
    print(index + 1, item, sep =".")
# 3.
for item in menu:
    print(item)
# 4. {} mô tả phần còn thiếu trong câu lệnh, có thể insert vào bằng {}.{}.format(x,y)
for index, item in enumerate(menu):
    print("{}.{}".format(index+1,item))

# update
print(*menu, sep=". ")
menu[4]= "Tôm hùm"
print(*menu, sep=". ")
# for index, item in enumerate(menu):
#     print("{}.{}".format(index+1,item))

# delete