def list_checker(array, input_value):
    for count in range(len(array)):
        if array[count] == input_value:
            return True
    return False

input_value = 5
array = [1, 2, 3, 4, 5]
exists = list_checker(array, input_value)

if exists:
        print(f"{input_value} exists in the array.")
else:
     print(f"{input_value} does not exist in the array.")