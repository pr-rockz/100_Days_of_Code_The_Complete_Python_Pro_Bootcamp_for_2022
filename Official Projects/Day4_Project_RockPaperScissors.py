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

game_images = [rock, paper, scissors]

computer_choice = random.randint(0,2)
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("\nYour Choice:", end='')
if your_choice > 2 or your_choice < 0:
    print("\nWrong choice. You lose!")
    exit()
else:
    print(game_images[your_choice])

print("\nComputer's Choice:", end='')
print(game_images[computer_choice])

if your_choice == computer_choice:
    print("\nIt's a draw!")
elif your_choice == 0 and computer_choice == 2:
    print("\nYou Win!")
elif your_choice == 2 and computer_choice == 0:
    print("\nYou Lose!")
elif your_choice > computer_choice:
    print("\nYou Win!")
else:
    print("\nYou Lose!")