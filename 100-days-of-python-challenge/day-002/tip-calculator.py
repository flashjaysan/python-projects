print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_number = int(input("how many people to split the bill? "))
per_person = total_bill * (1 + percentage / 100) / people_number
print(f"Each person should pay ${per_person:.2f}.")
