import random
#rock
Rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("********WELCOME TO THE GAME********")
print("\n**********OUR CHOICES ARE**********")

print("\n\n\t '0' for rock \n\t '1' for paper \n\t '2' for scissors")
customer_choice = int(input("Enter your choice please : "))

image_choices = [Rock, Paper, Scissors]


if customer_choice >= 3 and customer_choice < 0 :
    print("you enter in valid number")
else:
    print(image_choices[customer_choice ])
    computer_choice = random.randint(0,2)
    print("computer choice is .........")
    print(image_choices[computer_choice])

    if customer_choice == 0 and computer_choice == 2:
        print("THE WINNER IS YOU 🤩🤩🤩🤩🤩 ")
    elif computer_choice == 0 and  customer_choice == 2:
        print("YOU LOSE 😡😡😡😡")
    elif computer_choice == customer_choice:
        print("YOU DROW")
    elif computer_choice > customer_choice:
        print("YOU LOSE 😡😡😡😡")
    elif computer_choice < customer_choice:
        print("THE WINNER IS YOU 🤩🤩🤩🤩🤩 ")  

 