print("Welcome to Treasure Island")
print('''
  88
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88



           88           88                                 88
           ""           88                                 88
                        88                                 88
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8

                                                 ''')
print("You mission is to find the  Treasure")

choice = input("You are at the cross road. Where do you want to go? Type 'right' or 'left' to choose: \n").lower()
if choice == "left":
    choice2 = input("You have come to lake.There is an island at the middle of the lake.Type 'wait' to wait for boat.Type 'swim' to swim across:\n ").lower()
    if choice2 =="wait":
        choice_of_door = input("Which door would you like to take? Blue or Red or yellow:\n ").lower()
        if choice_of_door == "yellow":
            print("You win")
        elif choice_of_door == "Red":
            print("Burn by fire. Game Over!")
        elif choice_of_door == "Blue":
            print("Eaten by beast. Game Over!")
        else:
            print("Game Over!")

    else:
        print("Attacked by trout. Game Over!!")
else:

    print(" Fall into a hole!. Game Over!!!")
    exit()