number_one = int(input("Enter integer one: "))

number_two = int(input("Enter integer one: "))

number_three = int(input("Enter integer one: "))


maximum = max(number_one,number_two,number_three)

minimum = min(number_one,number_two,number_three)

total = number_one + number_two + number_three

middle_number = total - minimum - maximum

print(minimum,middle_number,maximum)