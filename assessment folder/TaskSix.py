totalScore = 0
average = 0
for score in range(1, 11):
		
	userScore = float(input("Enter score "));
	
	if userScore % 2 == 0:
	
		totalScore = totalScore + userScore
		average = totalScore / score
		
print("Average =",average)

