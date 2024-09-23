print("Welcome to Python Pizza Deliveries")
size = input(("What size of pizza do you want?,  S/M/L: ")).lower()
Add_pepperoni = input("Do you want a pepperoni? Y/N: ").lower()
extra_cheese = input("Do you want extra cheese?, Y/N: ").lower()

bill = 0
if size == "s":
    bill += 15

elif size == "m":
    bill += 20

elif size == "l":
    bill += 25

if Add_pepperoni == "y" and size == "s":
    bill +=2
else :
    bill += 3
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is  ${bill}")