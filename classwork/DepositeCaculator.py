"""
prompt user to enter deposit amounts 
store as deposit amount
prompt user to enter withdraw amounts
store as withdrawal 
add all deposit - withdrawal
display result
"""
total_amount = 0
counter = 0

deposited_amount = float (input("Enter amount to deposited"))

while deposited_amount!= -8:
	total_amount += deposited_amount
	deposited_amount = float (input("Enter amount to deposited"))
	print(total_amount  ) 
	
	
	


