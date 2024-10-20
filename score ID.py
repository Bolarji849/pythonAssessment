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