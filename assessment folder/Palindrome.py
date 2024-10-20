def reverse(number):
	reverse = 0
	user_inputed_number = number




	while number != 0:
		reverse = reverse * 10 + number % 10
		number = number / 10
		



		return reverse


def main():
	number = int(input("Enter the number: "))
	reversed_number = reverse(number)
	print(reversed_number)
	#if number == reversed_number:
		#print(reversed_number)


		#print("it's a palindrome")
	#else:
		#print("it's not a palindrome")






main()
