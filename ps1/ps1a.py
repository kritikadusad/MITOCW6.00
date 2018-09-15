# Problem Set 1
# Name: Kritika Dusad
# Collaborators: None
# Time Spent:

bal = float(raw_input('Enter the outstanding balance on your credit card:'))
APR = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
minPR = float(raw_input('Enter the minimum monthly payment rate as a decimal:'))
tot = 0

for m in range (1,13):
	print 'Month:', m
	minpay = round(minPR * bal, 2)
	intpay = round((APR / 12) * bal, 2)
	ppay = round(minpay - intpay, 2)
	bal = round(bal - ppay, 2)
	tot = tot + intpay + ppay
	print 'Minimum monthly payment:$', minpay
	print 'Principle paid:', ppay
	print 'Remaining balance:', bal
print 'RESULT\nTotal amount paid:', tot
print 'Remaining balance:', bal


