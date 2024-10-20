color = ['oragan', 'banana','apple']

list(enumerate( color))
print(color)



for index, value in enumerate(color):
	print(f'{index}: {value}')


Student_tuple = ['Alice',[98,9,7]]

First_name, grade = Student_tuple

First_name = 'Alice'

grade = [98,9,7]

print(f'{First_name}:{grade}')