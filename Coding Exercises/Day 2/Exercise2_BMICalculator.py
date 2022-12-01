# Calculates the BMI of a person based on the inputs given by them

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight)/(float(height)*float(height))
print(int(bmi))