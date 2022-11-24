import random

user_points = 0
computer_points = 0
options = ["rock", "paper", "scissors"]

random_number = random.randint(0, 2)
computer_pick = options[random_number]
print(computer_pick)
while True:
    user_input = input(
        "Enter Rock / Paper/ Scissors or type Q to quit: ").lower()

    if user_input == "q":
        break

    elif user_input not in options:
        print("ENTER A VALID INPUT ")
        continue

    if user_input == "scissors" and computer_pick == "paper":
        print("YOU WON!")
        user_points += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("YOU WON!")
        user_points += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("YOU WON!")
        user_points += 1

  # TIE

    if user_input == "scissors" and computer_pick == "scissors":
        print("Its a tie!")

    elif user_input == "paper" and computer_pick == "paper":
        print("its a tie")

    elif user_input == "rock" and computer_pick == "rock":
        print("its a tie")

    else:
        print("YOU LOST")
        computer_points += 1

print("You won " + str(user_points) + " times.")
print("Computer won " + str(computer_points) + " times.")
print("GOODBYE")
