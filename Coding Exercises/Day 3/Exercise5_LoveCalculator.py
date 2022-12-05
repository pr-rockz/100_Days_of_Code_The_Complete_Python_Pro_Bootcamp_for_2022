# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.upper() + name2.upper()
true = 0
true=name.count('T')+name.count('R')+name.count('U')+name.count('E')
love = 0
love = name.count('L') + name.count("O") + name.count("V") + name.count("E")
ct = int(str(true) + str(love))

if ct < 10 or ct > 90:
    print(f"Your score is {ct}, you go together like coke and mentos.")
elif ct > 40 and ct < 50:
    print(f"Your score is {ct}, you are alright together.")
else:
    print(f"Your score is {ct}.")