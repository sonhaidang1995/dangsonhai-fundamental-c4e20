name = input("Enter your name: ")
name_lowercase = name.lower()
single_word = name_lowercase.split()
join_word = " ".join(single_word)
new_name = join_word.title()
print("Updated: ",new_name)