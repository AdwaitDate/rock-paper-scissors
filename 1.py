print("Welcome To This Computer Game\n")

playing = input("Do you want to Play\nPlease Enter Yes or NO: ")

if playing.lower() == "yes":
    print("Okay Lets Play")

else:
    quit()

Question1 = input("What Does cpu Stand For ")
if Question1.lower() == "central processing unit":
    print("Your Answer is Correct!")
else:
    print("Your Answer is Incorrect")

Question2 = input("What Does gpu Stand For ")
if Question2.lower() == "gpu":
    print("Your Answer is Correct!")
else:
    print("Your Answer is Incorrect")

Question3 = input("What Does Ram Stand For ")
if Question3.lower() == "random access memory":
    print("Your Answer is Correct!")
else:
    print("Your Answer is Incorrect")

Question4 = input("What Does com Stand For ")
if Question4.lower() == "computer":
    print("Your Answer is Correct!")
else:
    print("Your Answer is Incorrect")
