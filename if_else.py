age = int(input("Please enter your age: "))

if 0<age<=18:
    print("Since you are", age, "years old, you are a Minor")

elif 18<age<=60:
    print("Since you are", age, "years old, you are an Adult")

elif 60 < age <= 100:
    print("Since you are", age, "years old, you are a Senior Citizen")

else: 
    print("You entered an invalid number, run the program again and enter an age between 1 and 100")
