user_first_input = int(input("Eneter first number "))
if user_first_input < 0:
	print("invaild input")


user_second_input = int(input("Eneter second number "))
if user_first_input < 0:
	print("invaild input")


user_third_input = int(input("Eneter third number "))
if user_first_input < 0:
	print("invaild input")







def minimum( number1,  number2, number3):
	lowest = number1
	if lowest > number2: 
		lowest = number2
	if lowest > number3: 
		lowest = number3 
	
	return lowest
	
print(minimum(user_first_input,user_second_input,user_third_input))