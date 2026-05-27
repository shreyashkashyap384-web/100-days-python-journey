# Welcome message for the user
print("Welcome to the tip calculator!")

# Taking the total bill amount as input and converting it to float
bill = float(input("What was the total bill? $\n"))

# Taking the tip percentage as input and converting it to integer
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))

# Taking the number of people to split the bill
people = int(input("How many people to split the bill? \n"))

# Calculating the total bill including tip
total_bill = bill + (bill * tip/100)

# Calculating how much each person should pay
result = total_bill / people

# Rounding the result to 2 decimal places
payment = round(result, 2)

# Displaying the final amount each person should pay
print(f"Each person should pay: {payment}")