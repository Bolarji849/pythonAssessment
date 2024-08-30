userput = int(input("Enter a number: "))

count = 1
counter = 1
while(counter <= 10):
	count = userput * counter
	print(f"{userput} {'*'} {counter} {'='} {count} ") 
	counter+=1 

