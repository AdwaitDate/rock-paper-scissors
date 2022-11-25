import random

# top_of_range = input("ENTER A NUMBER: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print("ENTER A NUMBER GREATER THAN ZERO")
#         quit()
# else:
#     print("ENTER A NUMBER NEXT TIME")
#     quit()
print(" \n\n\n                                        WELCOME TO QUIZ GAME  ")
guesses = 0

random_number = random.randint(0, 10)

while True:
    guesses += 1
    user_input = input("MAKE A GUESS: ")

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("PLEASE ENTER A NUMBER NEXT TIME")
        continue

    if user_input == random_number:
        print(" YAY YOU GOT IT CORRECT ")
        break
    else:
        if user_input > random_number:
            print("YOUR NUMBER WAS GREATER THAN SYSTEM GENERATED NUMBER")
        else:
            print("YOUR NUMBER WAS LOWER THAN SYSTEM GENERATED NUMBER")


print("You got it in " + str(guesses) + " guesses")
