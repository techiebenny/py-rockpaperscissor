import random
from time import sleep

# created by benny 
# V1.2

""" git: techiebenny """

#Conversion Table
option = {
    1: "Rock",
    2: "Paper",
    3: "Scissor"    
}
#logic part 
Options = {
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


    result = (Options[user_choice][computer_choice])

    sleep(.500)
    print (result + "\n")
