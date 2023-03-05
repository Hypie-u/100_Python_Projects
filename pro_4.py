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

pc_choice = random.randint(0,2)
choose = int(input("What do you choose ? Type 0 for rock,  1 for Paper, 2 for Scissors.\n"))
if choose >= 3 or pc_choice < 0:
    print("You typed an invalid number, you lose")
else:
    game_images=[rock, paper, scissors]

    print(game_images[choose])
    print(game_images[pc_choice])

    if choose == 0 and pc_choice == 2:
        print("You win!")
    elif choose == 2 and pc_choice == 0:
        print("You lose")
    elif pc_choice > choose:
        print("You lose")
    elif  choose > pc_choice:
        print("You wins!")
    else:
        print("it is a draw")