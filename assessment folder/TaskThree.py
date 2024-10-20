average = 0
totalScore = 0

for i in range(1, 11):
		
	userScore = float(input("Enter score "));
	
	totalScore =  totalScore + userScore;
	
	average = totalScore / userScore
		
print("sum =",totalScore)
print("average =",average)