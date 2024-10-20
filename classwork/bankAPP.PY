balance = 0
user_input = input("Enter option 1 to deposit or 2 to withdraw or 0 to end: ")

while True:
	if user_input =='1':
		amount = float(input("Enter amount:"))
		balance += amount
	elif user_input  == '2':
			amount = float(input("Enter amount:"))
			if balance < amount:
				print("insufficient fund")
			else:
				balance -= amount
		elif user_input == '3':
			print("your balance is", balance)



	














