# Making a Tip Calculator based on the inputs given by the user

print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
percent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

bill_per_person = (( (total_bill * percent_tip) / 100) + total_bill)/ num_of_people
print(f"Each person should pay: ${bill_per_person:.2f}")