print("Welcome to my Computer quiz game\n")
play_input = input("Do you want to play the game?\n\nEnter 'yes' to start and 'enter' to exit\n")

if play_input.lower() != "yes":
    print("Okay Cool, See you again :)")
    quit()

score = 0

questions = {
    "What does CPU stand for?": "CENTRAL PROCESSING UNIT",
    "What does GPU stand for?": "GRAPHICAL PROCESSING UNIT",
    "What does RAM stand for?": "RANDOM ACCESS MEMORY",
    "What does ROM stand for?": "READ ONLY MEMORY",
    "What does PSU stand for?": "POWER SUPPLY"
}

for question, correct_answer in questions.items():
    answer = input(question + "\n").strip().upper()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("_______________________________________________________________________")

print("You got",score,"questions correct")
print("You have scored",((score/len(questions))*100),"%")
