# import random
# user_action=input("enter a choice(rock,paper,scissors):")
# possible_action=("rock","paper","scissors")
# computer_action=random.choice(possible_action)
# print("you chose(user_action),computer chose(computer_action)")

# if user_action==computer_action:
#     print("draw")
# elif user_action=="rock":
#     if computer_action=="scissors":
#         print("rock smash scissor! you win!")
#     else:
#         print("paper cover rock! you lose!")
# elif user_action=="paper":
#     if computer_action=="rock":
#         print("paper cover rock! you win!")
#     else:
#         print("scissor cut paper! you lose!")
# elif user_action=="scissor":
#     if computer_action=="paper":
#         print("scissor cut paper! you win!")
#     else:
#         print("rock smash scissor! you lose!")

import random
choices=["rock","paper","scissor"]
computer=random.choice(choices)
player=None

while player not in choices:
    player=input("rock,paper,or scissor?:")
if player=="computer":
    print("computer:",computer)
    print("player:",player)
    print("Tie")
elif player=="rock":
    if computer=="paper":
        print("computer:",computer)
        print("player:",player)
        print("you lose!")
    if computer=="scissor":
        print("computer:",computer)
        print("player:",player)
        print("you win!")
elif player=="scissor":
    if computer=="rock":
        print("computer:",computer)
        print("player:",player)
        print("you lose!")
    if computer=="paper":
        print("computer:",computer)
        print("player:",player)
        print("you win!")
elif player=="paper":
    if computer=="scissor":
        print("computer:",computer)
        print("player:",player)
        print("you lose!")
    if computer=="rock":
        print("computer:",computer)
        print("player:",player)
        print("you win!")
