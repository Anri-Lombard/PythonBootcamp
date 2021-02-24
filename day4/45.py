import random

# Rock
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

my_number = input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")
options = [Rock, Paper, Scissors]
my_choice = options[int(my_number)]
their_choice = options[random.randint(0, 2)]

print(my_choice)
print("\nComputer chose:\n")
print(their_choice)

if (my_choice == Rock and their_choice == Scissors) or (my_choice == Paper and their_choice == Rock) or (my_choice == Scissors and their_choice == Paper):
    print("You win")
elif my_choice == their_choice:
    print("You draw")
else:
    print("You lose")