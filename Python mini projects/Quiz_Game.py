print("Welcome to my Computer quiz game\n")
play_input = input("Do you want to play the game?\n\nEnter \'yes\' to strart and \'enter\' to exit\n")

if play_input.lower() != "yes":
    quit("Okay Cool, See you again :)")

score = 0
answer = input("What does CPU stand for?\n").title()
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?\n").title()
if answer == "Graphical Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?\n").title()
if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for?\n").title()
if answer == "Read Only Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?\n").title()
if answer == "Power Supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("_______________________________________________________________________")

if score == 5:
    print("\nScore:",score)
    print("Congratulations, you got Perfect Score!")

elif score == 4 or score == 3:
    print("Score:",score)
    print("Congratulations, you got Good Score!")

elif score == 2 or score == 1:
    print("Score:",score)
    print("Try Again, you may get Good Score!")


elif score == 0:
    print("Score:",score)
    print("Better Luck next time!")