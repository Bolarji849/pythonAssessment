
totalScore = 0

for score in range(1, 11):
		
	userScore = float(input("Enter score "));
	
	if score % 2 == 0:
	
		totalScore = totalScore + score
		
		
print("sum =",totalScore)
