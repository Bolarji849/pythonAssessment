'''zeros = []
for_in range(4):
	zeros.append(0)


print(zeros)

lst_zeros = []


for - in range(5):
	lst_zeros.append(zeros)

'''


lst_zeros = [[0] * 4 for _ in range(5)]

lst_zeros = [[0] * 4] * 5 


print(lst_zeros)

for row in range(len(lst_zeros)):
	for col in range(len(lst_zeros[row])):
		print(lst_zeros[row][col],end= " ")
	print()





