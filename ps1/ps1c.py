# Problem Set 1
# Name: Kritika Dusad
# Collaborators: None
# Time Spent:

starting_balance = float (raw_input('Enter the outstanding balance on your credit card:'))
AnnualInterest = float (raw_input('Enter the annual credit card interest rate as a decimal:'))


MonthlyInterestRate = AnnualInterest/12.0

# Initializing variables
remaining_balance = starting_balance
monthly_lower = round(remaining_balance/12.0, 2)
monthly_higher = round((remaining_balance * (1 + MonthlyInterestRate)** 12.0)/12.0, 2)

# Monthly payment loop.
while True:
	monthly_middle = round((monthly_higher + monthly_lower)/2.0, 2)
	prev_to_middle = monthly_middle - 0.01
		
	# Remaining balance calculation loop for monthly_middle.
	remaining_balance = starting_balance 
	prev_balance = starting_balance 
	for month in range(1,13):
		interest_payment = MonthlyInterestRate * remaining_balance
		remaining_balance += interest_payment
		prev_balance += interest_payment
		remaining_balance -= monthly_middle
		prev_balance -= prev_to_middle
		if remaining_balance <= 0:
			break

	if remaining_balance > 0:
		monthly_lower = monthly_middle
	elif remaining_balance == 0:
		monthly_payment = monthly_middle
		break
	else:
		monthly_higher = monthly_middle

	if prev_balance > 0 and remaining_balance < 0:
		monthly_payment = monthly_middle
		break


print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', monthly_payment
print "Number of months needed:", month
print "Balance:", remaining_balance