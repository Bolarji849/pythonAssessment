def square(number ):
	if number < 0:
		raise ValueError("Invalid  number")

			
	if number % 5 == 0:
		result = number ** (1/2)
		return result
	
	else:
		number = number / 5
		return number
	
	
	
	

	
