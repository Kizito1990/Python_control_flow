#Check the heigth of the game player
height = float(input(" Enter your height :"))
bill = 0
if height >= 120:
    print("Welcome to the rollercoaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("Children Ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth Ticket is $7")

    elif age >=45 and age <= 65:
        print("Everything is going to be alright, You acn ride for free")

    else:
        bill = 12
        print("Adult Ticket is $12")


    photo_taken = input("Do you want your phot taken: Y/N: ").lower()
    if photo_taken == "Y":

        bill +=bill

    print(f"Total bill is {bill}")

else:
    print("You can't play the rollercoaster, you have to grow taller")