def my_discount(price,discount):
	if price < 0 and discount < 0:
		raise ValueError("Invalid  figure")

	discount_percentage = (discount/100) * price
	
	Finial_amount = price - discount_percentage
	
	return Finial_amount

