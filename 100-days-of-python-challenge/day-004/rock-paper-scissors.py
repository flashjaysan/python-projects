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

import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('rock, paper or scissors? ').lower()

print(f'You chose {user_choice}.')
if user_choice == 'rock':
  print(rock)
elif user_choice == 'paper':
  print(paper)
elif user_choice == 'scissors':
  print(scissors)

print(f'The computer chose {computer_choice}.')
if computer_choice == 'rock':
  print(rock)
elif computer_choice == 'paper':
  print(paper)
elif computer_choice == 'scissors':
  print(scissors)

if computer_choice == user_choice:
  print('It\'s a draw.')
elif computer_choice == 'rock' and user_choice == 'paper' or computer_choice == 'paper' and user_choice == 'scissors' or computer_choice == 'scissors' and user_choice == 'rock':
  print('You win.')
else:
  print('You lose.')
