"""write a program that collect score of student and calculate the averag e"""

total_score = 0
count = 0
score_of_student = 0
while score_of_student != -1:
	score_of_student = int(input("Enter score: "))
	
	total_score += score_of_student 
	count = count + 1
	
total_average = count / total_score 
		
print(total_average)
	

	
	
	




