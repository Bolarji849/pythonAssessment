count = 0
totalScore = 0
while True:
		
	userScore = float(input("Enter score "));
	
	if userScore >= 0 and userScore <= 100:
		totalScore += userScore
		count+=1
		
	if count == 10:
		print(" Sum =",totalScore)
		break


