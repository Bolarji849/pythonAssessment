"""
write a program that calculate sum of mutilple of 10 between 1 to 20_000.
"""
sum_Total = 0
for number in range(1,20_000,10):
	sum_Total = sum_Total + number
print(sum_Total)
