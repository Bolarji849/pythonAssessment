
try:

	row = int(input("ENTER ROW: "))

	column =int(input("ENTER column: "))



	lst_numbers = [[0] * row for _ in range(column)]



	for ro in range(len(lst_numbers)):
		for col in range(len(lst_numbers[ro])):
			product = col * ro 
			print(product,"\t",end= " ")

		print()

except(Exception):
	
	print("CALM DOWN TRY NOT TO SMOKE ANYMORE")