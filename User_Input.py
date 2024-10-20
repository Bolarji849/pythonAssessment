'''collect some numbers in your terminal until the user is done display all the number in a list'''

data = 0
number = []
total = 0
cout = 0
average = 0
while data != -1:

	data = int(input("Enter number: "))
	if data != -1:
		number += [data]
		cout += 1
for i in number:
	total += i
	
if cout > 0:
	
	average = total / cout
	print("Average",average)
else:
	print(number)

