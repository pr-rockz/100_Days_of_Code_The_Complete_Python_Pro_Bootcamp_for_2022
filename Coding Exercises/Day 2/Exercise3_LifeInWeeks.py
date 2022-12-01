# Prints the days, weeks and years a person has got until he/she turns 90

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year = 90 - int(age)
months = year * 12
weeks = year * 52
days = year * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")