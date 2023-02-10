# Welcome message
print('Welcome to the tip calculator\n')

# Ask user for total bill, save into the variable
total_bill = float(input('What was the total bill? $'))

# Ask user for percentage_tip, save into the variable
percentage_tip = int(input('What percentage tip would you like to give? 10, 12, 15, or 18? '))

# Ask user for how many people to split the total bill, save into the variable
people_split = int(input('How many people to split the bill? '))

# Calculation of adding tip into total bill
bill_include_tip = total_bill * (1 + (percentage_tip / 100))

# Calculation of dividing the total bill with tip into splits
bill_per_person = bill_include_tip / people_split

# formatting the result by rounding into two numbers and makes two decimal places if its one or no decimal.
result = round(bill_per_person, 2)
result = "{:.2f}".format(result)

# Print last statement
print(f'Each person should pay: ${result}')

