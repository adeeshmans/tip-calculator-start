
print("Welcome to the Tip Calculator")
print("")

# Get input and convert string to float / store in var
bill = float(input("What was your total bill? $"))
# Get input and convert string to int / store in var
tip = int(input("How much tip would you like to give? 10, 12,or 15? "))
# Get input and convert string to int / store in var
people = int(input("How many people would you like to split the bill with? "))

# Formula
tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# Final amount below rounds to 2 decimal points for certain bill amount
final_amount = round(bill_per_person, 2)
# This Final amount is more accurate for rounding to 2 dec points
final_amount ="{:.2f}".format(bill_per_person)

print(f"Each person pays: ${final_amount}")