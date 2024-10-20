score = int(input("Enter score:"))






if score > 100:
	print("Invalid score")
elif score >= 75 and score <= 100:
	print("Your grade is A")
elif score >= 65 and score < 75:
	print("Your grade is B")
elif socre >= 50 and score < 65:
	print("Your grade is C")
elif socre >= 40 and score <= 49:
	print("Your grade is D")
else:
	print(" failed")