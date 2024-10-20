score1 = 45
score2 = 50

scores = [45, 50, 78, 25, 94, 100]

print("string address after delacration",id(scores))


scores[1] = 80

print(scores)

print(score[1])

print(len(scores))


print("string address after modification", id(scores))


name = "jesse"

print("name address after declaration",id(name))

name+= "akerele"

print("name address after modification",id(name))

additional_scores = [45,56,76]

score += additional_scores

print(scores)

'''scores[0] += 10'''
for index in range(len(scores)):
	score[index]+=10
print(scores)

print(scores * 3)

print(score[-1])

'''for index in range((score)-1,0,-1):
	reverse_list.append(scores[index])
	#reverse_list += scores[index]]
'''
reverse_list += scores[::-1]

print(reverse_list)

socres.append(20) 
#you only use this method to add one thing

scores.extend([56, 33, 44])

y = [56, 33, 44]

y += scores

print(y)


