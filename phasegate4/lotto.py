import random

number = input("Enter number").split()

random_number = random.randrange(1,50)
random_number2 = random.randrange(1,50)
random_number3 = random.randrange(1,50)

for count in range(4+1):
	if number [0] == random_number and number [1] == random_number2 and number [2] == random_number3:
		print("YOU WON $5000")
	elif number [0]  == random_number and number [1] == random_number2 and number [2] == random_number2:
		print("YOU WON $4000")
	elif number [0] == random_number and number [1] != random_number2 and number [2] == random_number2:
		print("YOU WON $3000")
	elif number [0]  != random_number and number [1] != random_number2 and number [2] == random_number2:
		print("YOU WON $2000")
	
	else:
		print("you didnt getx it this time try again next time")








