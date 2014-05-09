#!usr/bin/python
#Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.
cost = int(raw_input("What is the cost? "))
tax_rate = float(raw_input("What is the tax rate? Please enter in decimal form. "))
tax = cost*tax_rate
print "Tax = " + str(tax)
print "Total cost = " + str(tax+cost)