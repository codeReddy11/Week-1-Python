secret_number = 9
attempts = 0
guessed_correctly = False

print("Hello! welcome to the Guessing Game")
print("Try to guess the number between 1 to 15")

while guessed_correctly == False:

    user_input = int(input("Enter your guess: "))

    attempts += 1

    if user_input == secret_number:
        guessed_correctly =True

    elif 15 >= user_input > secret_number:
        print("Too High! Try a lower number")

    elif 0 < user_input < secret_number:
        print("Too Low! Try a higher number")

    else:
        print("You entered", user_input,". guess the number between 1 and 15. Don't worry this attempt is not counted")
        attempts -=1

print(user_input)
print("Congrats you guessed it right")
print("you took", attempts, "attempts to guess the number")


    