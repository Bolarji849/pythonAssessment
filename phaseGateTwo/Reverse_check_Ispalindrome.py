

input_data = int(input("Enter the number: "))

def reverse(number):

	reverse = 0
	
	while number != 0:
		reverse = (reverse * 10) + number % 10
		number = number // 10
		

	return reverse


reverse(input_data)


def is_palindrome(number):
	
	if reverse(number) == input_data :
		print("it's a palindrome")
		
	if reverse(number) != input_data:
		print("it's not a palindrome")


is_palindrome(input_data)



