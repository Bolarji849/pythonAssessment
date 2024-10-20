

user_first_input = int(input("Eneter first number "))
if user_first_input < 0:
	print("invaild input")


user_second_input = int(input("Eneter second number "))
if user_first_input < 0:
	print("invaild input")


user_third_input = int(input("Eneter third number "))
if user_first_input < 0:
	print("invaild input")

 




def maximum( number1,  number2, number3):
	largest = number1
	if largest < number2: 
		largest = number2
	if largest < number3 : 
		largest = number3
	 
	return largest
	
	
print(maximum(user_first_input,user_second_input,user_third_input))