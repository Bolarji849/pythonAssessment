import random



count = 1
counter = 0 
counter2 = 0
tem = 0
total = 0

for i in range(1,11):
	random_number = random.randrange(1,100)
	random_number2 = random.randrange(1,100)
	
	if(random_number < random_number2):

		tem = random_number
		
		random_number = random_number2

		random_number2 = tem
	print(random_number,"-" ,random_number2)

	userinput = int(input("ENTER CORRECT ANSWER: "))
	
	total = random_number - random_number2
		
	if(total == userinput ):

		print(" correct ")
		counter = counter+1

	else:
		print(" incorrect ")
		counter2 = counter2+1


print("Total number of correct anwser is ", counter)

print("Total number of correct anwser is ", counter2)
