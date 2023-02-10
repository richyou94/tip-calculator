
print('Welcome to the tip calculator\n')

total_bill = float(input('What was the total bill? $'))

percentage_tip = int(input('What percentage tip would you like to give? 10, 12, 15, or 18? '))

people_split = int(input('How many people to split the bill? '))

bill_include_tip = round(total_bill * (1 + (percentage_tip / 100)), 2)

print(bill_include_tip)



# result = 0

# print(f'Each person should pay: ${result}')

