#Check the heigth of the game player
height = float(input(" Enter your height :"))
if height >= 120:
    print("Welcome to the rollercoaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        print("You will pay $5 to ride rollercoaster")
    elif age <= 18:
        print("You will pay $7 to play rollercoaster")
    else:
        print("You will pay $12 to play rollercoaster")

else:
    print("You can't play the rollercoaster, you have to grow taller")