# # Cách 1: Dùng biến để đếm số lần lặp
# count = 0
# while count <3:
#     print("Running...")
#     count += 1

# # Cách 2: Dùng biến trạng thái để kiểm soát vòng lặp
# count = 0
# loop = True
# while loop:
#     print("Running...")
#     count +=1
#     if count == 5:
#         loop = False

# Cách 3: Break: đã brake => dừng toàn bộ bộ, không quan tâm đến phần code bên dưới break.
# Nếu dùng loop thì phần code bên dưới loop vẫn được thực thi
count = 0
loop = True
while loop:
    print("Running...")
    count +=1
    if count ==5:
        # loop = False
        break
        print("Bye")