#Collecting users height in (cm) and  weight in (kg)
weight = float(input("Enter yur weight in kg: "))
height = float(input("Enter your height in cm: "))

BMI = round(weight / height **2)

if BMI <18.5:
    print(f" Your Bmi is {BMI}, You are underweight")
elif BMI < 25:
    print(f"Your Bmi is {BMI},You have normal weight")
elif BMI <= 30:
    print(f"Your Bmi is {BMI},You are overweight")
elif BMI < 35:
    print(f"Your Bmi is {BMI},You are are Obese")
else:
    print(f"Your Bmi is {BMI},You are clinically Obessed")




