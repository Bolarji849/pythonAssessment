def covert_dollars_to_niara(dollars: float):
	if type(dollar) not in [int, float]:
		return "invalid input"
	
	if dollars < 0:
		raise ValueError("Invalid  amount")

	RATE = 1550
	amount_to_naira = RATE  * dollars
	round_number = round(amount_to_naira,2)

	return round_number
	
	

	