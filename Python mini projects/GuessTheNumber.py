import random

number_range = input("Enter a number(maximum range):")
if number_range.isdigit():
    number_range = int(number_range)
    if number_range <= 2:
        print("Please enter a number which is greater than 1 next time")
        exit()

else:
    print("Please Enter a number next time.")
    exit()

random_number = random.randint(1,number_range)
guesses = 0

while True:
    guesses += 1
    guess_num = input("Enter a number:")

    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("Please enter a number next time")
        continue

    if guess_num == random_number:
        print("Horray!, your have guessed the number in",guesses,"guesses.")
        break
    elif guess_num > random_number:
        print("You guess number is above the number")
    elif guess_num < random_number:
        print("You guess number is below the number")