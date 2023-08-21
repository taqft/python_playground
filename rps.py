from random import randint

#create list of play options
choice = ["rock", "paper", "scissors"]

#give the computer a choice
computer = choice[randint(0,2)]

#the challenger enters the ring
player = False

while player == False:
    player = input("Rock, Paper, or Scissors? ")
    if player.casefold() == computer.casefold():
        print("Tie!")
    elif player.casefold() == "rock":
        if computer.casefold() == "paper":
            print("You lose!", computer.title(), "covers", player + ".")
        else:
            print("You win!", player.title(), "crushes", computer + ".")
    elif player.casefold() == "paper":
        if computer.casefold() == "scissors":
            print("You lose!", computer.title(), "cut", player + ".")
        else:
            print("You win!", player.title(), "covers", computer + ".")
    elif player.casefold() == "scissors":
        if computer.casefold() == "rock":
            print("You lose...", computer.title(), "crushes", player + ".")
        else:
            print("You win!", player.title(), "cut", computer + ".")
    else:
        print("Invalid play. Type carefully!")

    rematch = input("Try again?(Y/N) ")
    if rematch.casefold() == "y":
        #reach for the sky
        player = False
        computer = choice[randint(0,2)]
    else:
        print("Thanks for playing!")
        