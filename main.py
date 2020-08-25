import random

# created by benny

""" git: techiebenny """



print("welcome to rock paper scissors!")
player_name = input("Enter your name: ")

print("Hello " + player_name + "!")

print("Welcome to Rock Paper Scissor!")
# print("Choose \n 1: Rock \n 2: Paper \n 3: Scissor \n\n")

inputchoice = int(input("Choose \n 1: Rock \n 2: Paper \n 3: Scissor \n\n"))

option = {
    1: "Rock",
    2: "Paper",
    3: "Scissor"
}

user_choice = option[inputchoice]
computer_choice = random.choice(list(option.values()))

print("You have chosen " + user_choice)
print("Computer has chosen " + computer_choice)

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


result = (Options[user_choice][computer_choice])

print (result)
