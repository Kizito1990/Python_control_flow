#Ask user to input the number to check
number = int(input("Enter the number : "))

#check if the number is even or odd using if statement and modulo
if number % 2 == 0:
    print(f"The {number} is a an Even number")
else:
    print(f"The {number} is Odd number ")