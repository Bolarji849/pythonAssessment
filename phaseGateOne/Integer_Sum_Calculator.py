import random

random_number = random.randrange(1,100)
random_number2 = random.randrange(1,100)
print(random_number, random_number2)


userinput = int(input("Enter the sum of the two integers: "))

total = random_number +  random_number2

if(total == userinput ):
	print("true")
else:
	print("false")
	


