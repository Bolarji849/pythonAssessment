for digit in range(1000,3000):

	firstNumber = digit // 1000

	secondNumber = (digit // 100)%10

	thirdNumber = (digit // 10)%10

	fourNumber = (digit % 10)



	if (firstNumber % 2 == 0 and secondNumber % 2 == 0 and thirdNumber % 2 == 0 and fourNumber % 2 == 0):

		print( digit, end = " ,")


