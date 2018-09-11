# Problem Set 1
# Name: Kritika Dusad
# Collaborators: None
# Time Spent:

bal = float (raw_input('Enter the outstanding balance on your credit card:'))
APR = float (raw_input('Enter the annual credit card interest rate as a decimal:'))


MIR = APR/12.0
minpay = 0
rembal = bal

while rembal > 0:
	minpay += 10
	rembal = bal
	month = 0

	while month < 12 and rembal > 0:
		month += 1
		intpay = MIR * rembal
		rembal += intpay
		rembal -= minpay
rembal = round(rembal, 2)

print "RESULT"
print "Monthly payment to pay off debt in 1 year:", minpay
print "Number of months needed:", month
print "Balance:", rembal 



