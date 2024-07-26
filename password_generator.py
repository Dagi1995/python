import random
letter_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("********welcome to password_list generator********")


letter = int(input("How many letter you want in your password ? "))
symbol = int(input("How many symbol you want in your password ? "))
number = int(input("How many number you want in your password ? "))

password_list = []
for char in range(0 , letter):
    password_list+=random.choice(letter_list)

for char in range(0 , symbol):
    password_list+=random.choice(symbol_list)
    
for cahr in range(0 , number):
    password_list +=random.choice(number_list)

#to change the order
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password+=char

print(password)