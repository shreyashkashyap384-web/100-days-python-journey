import random

print("WELCOME TO THE ROCK PAPER SCISSOR GAME")
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
game = [rock, paper, scissors]
player1 = int(input(f"choose: 0 for rock{rock}, 1 for paper{paper} or 2 for scissors{scissors}"))
computer = (random.choice(game))
display1 = print(f"Computer chose: {computer}")
if player1 == 0 and computer == rock:
    print("Draw")
elif player1 == 0 and computer == paper:
    print("Rock lose by Paper, You lost !")
elif player1 == 0 and computer == scissors:
    print("Rock beats Scissors, You win !")
elif player1 == 1 and computer == rock:
    print("Paper beats Rock, You win !")
elif player1 == 1 and computer == scissors:
    print("Scissors beats Paper, You lost ! ")
elif player1 == 1 and computer == paper:
    print("Draw")
elif player1 == 2 and computer == scissors:
    print("Draw")
elif player1 == 2 and computer == rock:
    print("Rock beats Scissors, You lost !")
elif player1 == 2 and computer == paper:
    print("Scissors beats Paper, You win !")
else:
    print("Invalid input, Try again !!")
