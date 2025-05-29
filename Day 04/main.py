import random
choice = int(input(("What do you choose? Type 0 for rock, 1 for papers and 2 for scissors\n")))
if choice<0 or choice>2:
    print("You typed a wrong number!")
    exit()
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_image = [rock, paper, scissors]
print("You chose ")
print(game_image[choice])

comp_fin_choice =random.randint(0,2)
print("\n\nComputer chose ")
print(game_image[comp_fin_choice])


if (choice == 0 and comp_fin_choice ==1) or (choice == 1 and comp_fin_choice == 2) or (choice == 2 and comp_fin_choice == 0):
   print("You Lose")
elif (choice == 0 and comp_fin_choice ==2) or (choice == 1 and comp_fin_choice ==0) or (choice == 2 and comp_fin_choice == 1):
   print("You Win!")
elif (choice == 0 and comp_fin_choice ==0) or (choice == 1 and comp_fin_choice == 1) or (choice == 2 and comp_fin_choice == 2):
   print("You Draw")
