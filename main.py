import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images= [rock, paper, scissors]

user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n"))

if 0 <=  user_choice <= 2:
    print("You Choose: ")
    print(images[user_choice])

    print("Computer Choose: ")
    computer_choice = random.randint(0, 2)
    print(images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice > user_choice:
        print("You Lose!")
    else:
        print("Draw.")

else:
    print("Invalid input. Choose 0, 1 or 2")



