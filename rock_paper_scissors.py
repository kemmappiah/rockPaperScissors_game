import random
import string
import time

print("Welcome to the ROCK - PAPER - SCISSORS game\nCreated by EMMAPP\nThis is a ONE player game against the CPU")
player_name = input("Please enter your name: ")
checked = False
while True:
    rounds_number = input("Please enter number of rounds to play: ")
    if rounds_number not in string.digits:
        print("Enter a valid number")
        checked = True
    else:
        rounds_select = int(rounds_number)
        another_round = True
        rounds_count = 1
        cpu_score = 0
        player_score = 0
        while rounds_count <= rounds_select:
            print("ROCK")
            time.sleep(1)
            print("PAPER")
            time.sleep(1)
            print("SCISSORS")
            print("Shoot!")
            game_dict = {
                1: "rock",
                2: "paper",
                3: "scissors"
            }
            game_choice = input("Select 1 for ROCK, 2 for PAPER, 3 for SCISSORS: ")
            print("You choose ", game_dict[int(game_choice)])
            options = ["rock", "paper", "scissors"]
            cpu_choice = random.choice(options)
            print("CPU chooses ", cpu_choice)
            if game_choice == "1" and cpu_choice == "rock":
                print("RESULT - TIE!")
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "2" and cpu_choice == "paper":
                print("RESULT - TIE!")
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "3" and cpu_choice == "scissors":
                print("RESULT - TIE!")
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "1" and cpu_choice == "paper":
                print("Paper wraps rock - CPU Wins!")
                cpu_score += 1
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "1" and cpu_choice == "scissors":
                print("Rock beats Scissors  - You win!")
                player_score += 1
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "2" and cpu_choice == "rock":
                print("Paper wraps Rock - You win!")
                player_score += 1
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "2" and cpu_choice == "scissors":
                print("Scissors cuts Paper - CPU wins!")
                cpu_score += 1
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "3" and cpu_choice == "rock":
                print("Rock beats Scissors - CPU wins!")
                cpu_score += 1
                rounds_count += 1
                time.sleep(2)
                another_round = True
            elif game_choice == "3" and cpu_choice == "paper":
                print("Scissors cuts Paper - You win!")
                player_score += 1
                rounds_count += 1
                time.sleep(2)
                another_round = True
        print("\nGAME OVER\nFINAL SCORES:\n", player_name, "-", player_score, "\n", "CPU - ", cpu_score,
              "\n\nThank you for playing!\nCome back another time!")
        break


