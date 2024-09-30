userinput = int(input("Enter number range from 0 to 1000: "))

number1 = userinput // 100

number2 = (userinput //10)%10

number3 = (userinput % 10)

sum = (number1 + number2 + number3)

print(sum)