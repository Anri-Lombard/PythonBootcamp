print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

individual_bill = (float(bill) + (float(bill) * (int(percentage) / 100))) / int(split)
final = "{:.2f}".format(individual_bill)
print(f"Each person should pay: ${final}")