income = float(input('Enter your monthly income: '))
expenses = float(input('Enter your total monthly expenses: '))

monthly_savings = income - expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print('Your monthly savings are $' + str(monthly_savings) + '.')
print('Projected savings after one year, with interest, is: $' + str(projected_savings) + '.')
