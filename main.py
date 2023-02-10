
print('Welcome to the tip calculator\n')

total_bill = float(input('What was the total bill? $'))

percentage_tip = int(input('What percentage tip would you like to give? 10, 12, 15, or 18? '))

people_split = int(input('How many people to split the bill? '))

bill_include_tip = total_bill * (1 + (percentage_tip / 100))

bill_per_person = bill_include_tip / people_split
# It will be better if I can limit the result into two decimals
result = round(bill_per_person, 2)

print(f'Each person should pay: ${result}')

