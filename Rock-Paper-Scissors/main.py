import random

print("""Welcome!
         This is the Rock-Paper-Scissors game.

        How to play?
        1. You are playing against the computer.
        2. You are to choose an option from,
           R for Rock, P for Paper and S for Scissors.
        3. Rock beats Scissors (Rock Wins)
           Paper beats Rock (Papper Wins)
           Scissors beats Paper (Scissors Wins)

           So if you choose R - Rock and Computer choose S - Scissors,
           YOU WIN.
           If you choose P - Paper and Computer choose S - Scissors,
           YOU LOSE.

           Have Fun playing!


             """)

while True:
    # Options for users to enter when the game starts
    list = {
        "R" : "Rock",
        "P" : "Paper",
        "S" : "Scissors"
    }

    #Taking input(as choices) from the users
    user = input("""What's is your choice?
                    R for Rocks
                    P for Paper
                    S for Scissors

                    Choose one: """)
    #converts the user input to uppercase
    #even if the user entered a lower case letter
    user = user.upper()
    #possible options to choose from
    pos_options = ["R", "P", "S"]
    #Defining CPU's choice
    computer = random.choice(pos_options)

    #Condition, if it's a tie (user move == computer move)
    if (user == computer):
        print(f"Players' move: Player({list[user]}) : CPU({list[computer]}).\n")
        print(f"\nYou chose {list[user]}, computer chose {list[computer]}, its's a TIE!\n")

    #Condition, to check for win or lose
    elif (user == "R"):
        if (computer == "S"):
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("Rock beats scissors! You WIN!")
            break
        else:
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("""
            Paper beats rock! You LOSE!
            CPU win """)
            break
    elif (user == "P"):
        if (computer == "R"):
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("Paper beats rock! You WIN!")
            break
        else:
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("""
            Scissors beats paper! You LOSE!
            CPU win
             """)
            break
    elif (user == "S"):
        if (computer == "P"):
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("Scissors beats paper! You WIN!")
            break
        else:
            print(f"\nPlayers' move: Player({list[user]}) : CPU({list[computer]})\n")
            print("""
            Rock beats scissors! You LOSE!
            CPU win """)
            break
    else:
        print("""
                You entered an invalid input.

                Play again...!

                """)
        continue

