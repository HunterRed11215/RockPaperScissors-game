import random

count_player = 0
count_cpu = 0
print("---------------WELCOME! TO THE ULTIMATE ROCK, PAPER, SCISSORS GAME!!!---------------")
name = input("Player! Enter your Name: ")
print("-----------RULES/GUIDELINES-----------")
print("1. Game is of 5 points. Whoever score 5 points first wins the Championship.")
print("2. For each round win, you will get 1 point")
print("3. For tie both will get 0 point each")
print("4. If you want to quit just type \'q\' or \'quit\'")
print()
print("LET'S THE BATTLE BEGIN!!!")
print()
while count_cpu != 5 and count_player != 5:
    print(f"Computer: {count_cpu} - {count_player}: {name}")
    print("...ROCK...")
    print("...PAPER...")
    print("...SCISSORS...")
    
    player_input = input(f"{name}, your turn:  ").lower()
    if (player_input == "q" or player_input == "quit"):
        print("Okay! Bye! Coward!")
        break
    cpu_input = random.randint(1, 3)
    if cpu_input == 1:
        cpu = "rock"
    elif cpu_input == 2:
        cpu = "paper"
    elif cpu_input == 3:
        cpu = "scissors"
    print(f"Computer's Input: {cpu}")
    print("SHOOT")
    print()

    if player_input == cpu:
        print("It\'s a DRAW")
        print()
    elif player_input == "rock":
        if cpu == "scissors":
            print(f"{name} WIN!")
            print()
            count_player += 1
        elif cpu == "paper":
            print("Computer WIN!")
            count_cpu += 1
            print()
    elif player_input == "scissors":
        if cpu == "rock":
            print("Computer WIN!")
            count_cpu += 1
            print()
        elif cpu == "paper":
            print(f"{name} WIN!")
            count_player += 1
            print()
    elif player_input == "paper":
        if cpu == "rock":
            print(f"{name} WIN!")
            count_player += 1
            print()
        elif cpu == "scissors":
            print("Computer WIN!")
            count_cpu += 1
            print()
    else:
        print("Something went wrong")
        print()

print("!!!FINAL SCORE!!!")
print(f"{name}: {count_player} - {count_cpu} :Computer")

if count_cpu == 5:
    print("COMPUTER beats you! Better luck next time.")
elif count_player == 5:
    print(f"{name}! You have WON THE CHAMPIONSHIP!!!")