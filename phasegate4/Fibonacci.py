userInput = int(input("Enter the number:"))
a = 0
b = 1
print (a)
print(b)
print(b)
c = b
for count in range(1,userInput,1):
	a = b
	b = c
	c = a+b
	print(c)