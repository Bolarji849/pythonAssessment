def get_swap_number(array):
	for count in range(len(array)):
		if(count % 2 != 0):
			temp = array[count]
			array[count] = array[count-1]
			array[count-1] = temp
	return array



	
