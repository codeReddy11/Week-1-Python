while True:
    num = int(input("Enter number greater than 20: "))

    if num > 20:
        print("you entered", num)
        break
    else:
        print("you entered invalid number, try again")