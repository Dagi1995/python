import random
names_string = input("enter names and seperate by comma : ")
names=names_string.split(", ")
# len_name =len(names)
# choice_random = random.randint(0,len_name-1)
# unlucky_person =names[choice_random]

unlucky_person =random.choice(names)

print(f"today the bill is covered by {unlucky_person }")
# print(len_name)