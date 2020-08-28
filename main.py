import random

# created by benny 
# V1.1

""" git: techiebenny """



print("welcome to rock paper scissors!")
player_name = input("Enter your name: ")

print("Hello " + player_name + "!")

print("Welcome to Rock Paper Scissor!")


# Get User Input

inputchoice = 0

while True:
    inputchoice = input("Choose \n 1: Rock \n 2: Paper \n 3: Scissor \n\n")
    
    while not inputchoice.isdigit():
        inputchoice = input("Please input a number from 1-3!! : ")
        continue

    inputchoice = int(inputchoice)
    
    if(inputchoice > 3 or inputchoice < 0):
        print("Wrong Choice Entered, Please try again.")
        continue

    else:
        break


#Conversion Table
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
