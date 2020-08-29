import random
from time import sleep

# created by benny 
# V1.3

""" git: techiebenny """



print("welcome to rock paper scissors!")
player_name = input("Enter your name: ")

"""
stats = {
    "games": 0,
    "player": 0,
    "cpu": 0,
    "draw": 0
}
"""


print("Hello " + player_name + "!")

print("Welcome to Rock Paper Scissor!")


inputchoice = 0
#Conversion Table
option = {
    1: "Rock",
    2: "Paper",
    3: "Scissor"    
}
#logic part 
Choices = {
    "Rock" : {
        "Rock": "Draw",
        "Paper": "Lose",
        "Scissor": "Win" 
    },
    "Paper" : {
        "Paper": "Draw",
        "Rock": "Win",
        "Scissor": "Lose" 
    },
    "Scissor" : {
        "Scissor": "Draw",
        "Rock": "Lose",
        "Paper": "Win"
    }
}

while True:
    inputchoice = input("Choose \n 1: Rock \n 2: Paper \n 3: Scissor \n\n")
    
    if not inputchoice.isdigit():
        print("Enter a choice as number displayed")
        continue

    inputchoice = int(inputchoice)

    if not(inputchoice >=1 and inputchoice <=3 ):
        print("Wrong Choice Entered, Please try again.")
        continue
        
        #inputchoice = input("Please input a number from 1-3!! : ")

    user_choice = option[inputchoice]
    computer_choice = random.choice(list(option.values()))

    print("You have chosen " + user_choice)
    print("Computer has chosen " + computer_choice)


    result = (Choices[user_choice][computer_choice])

    print (result + "\n")
    sleep(.500)

    replay = input("\nPress Y to play again. \t :")
    if(replay.lower() == "y" ):
        continue
    else:
        print("\n\nThanks for playing!")
        sleep(1.500)
        break