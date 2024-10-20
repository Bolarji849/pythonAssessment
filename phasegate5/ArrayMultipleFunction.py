def get_Ascending_number(array):
	for index in range(len(array)):
		for count in range(len(array)-1-index):
			if(array[count] > array[count+1] ):
				array[count] =  array[count] + array[count+1]
				array[count+1] = array[count] - array[count+1]
				array[count] = array[count] - array[count+1]
	print(array)

	for _ in range(len(array)):
		product_third_position *= array[2]
		print(array)
get_Ascending_number([5,2,7,1,8,2])



def get_Descending_number(array):
	for index in range(len(array)):
		for count in range(len(array)-1-index):
			if(array[count] < array[count+1] ):
				array[count] =  array[count] + array[count+1]
				array[count+1] = array[count] - array[count+1]
				array[count] = array[count] - array[count+1]
	print(array)

get_Descending_number([5,2,7,1,8,2])




