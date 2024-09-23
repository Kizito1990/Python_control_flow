print("Welcome to Love Calculator")
#Ask the lowers to put their names to check if they will match each other.
name1  = input("Enter the first lover's name: ").lower()
name2 = input("Enter the second Lover's name: ").lower()

#Count how many times each letters in the lovers names appeared using count function
combined_names = name1 + name2
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t+r+u+e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e
#Add the the number times the letters appeared in the two words and converted back to integer
true_love = int(str(true) + str(love))


if (true_love < 10) or (true_love > 90):
    print(f"Your Love score is {true_love}. You are like coke and mento together")

elif (true_love <= 45) and (true_love <= 50):
    print(f"The true love is {true_love}. You are both good  together")
else:
    print(f"You love score is {true_love}.")
