def covert_dollars_to_niara(dollars):
	if dollars < 0:
		raise ValueError("Invalid  amount")

	
	CONSTANT_RATE = 1550
	amount_to_naira = CONSTANT_RATE  * dollars
	round_number = round(amount_to_naira,2)

	return round_number
	
	

	