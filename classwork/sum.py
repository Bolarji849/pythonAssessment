'''
prompt user to enter number one 
store as number one
prompt user to enter number two
store as number two
prompt user to enter number three
store as number three
add all the numbers one number two number three divide by 3
display result as average
'''

number_one = int(input("Enter a number: "))
number_two = int(input("Enter a number: "))
number_three = int(input("Enter a number: "))

sum = number_one + number_two + number_three
average = sum/3
print("The average is",average)