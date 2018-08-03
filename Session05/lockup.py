dictz = {
    "cc": "Cục cưng, động vật quý hiếm",
    "hc": "Học, học nữa, học mãi",
    "pt": "party, tổ đội trong game nhập vai",
    "eny": "Bún đậu mắm tôm",
    "any": "Thằng đầu tôm",
    "ns": "Nói",
    "ngta": "Con nhà người ta, đẹp trai, nhà giàu",
    "lm": "Làm, làm nữa, làm mãi",
    "r": "Đã xong rồi"
}
while 1:
    for k in dictz.keys():
        print(k, end ="\t")
    print("")
    print("*"*20)
    word = input("Your word? ")
    if word in dictz:
        print("*"*20)
        print(word,dictz[word],sep=": ")
        print("*"*20)
    else:
        print("*"*20)
        command = input("Not found in dictionary, you want update? (Y/N)").upper()
        if command == "Y":
            print("*"*20)
            k = input("what do you want to update? ")
            dictz[word] = k
        elif command == "N":
            print("*"*20)
            print("Bye bro")
            break
        else:
            print("*"*20)
            print("Bye bro")
            break
    