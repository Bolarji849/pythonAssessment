def calculate_for_largest(numbers):
    largest = numbers[0]
    for count in range(len(numbers)):
        if numbers[count] > largest:
            largest = numbers[count]
    return largest

array = [1, 7, 3]
print(calculate_for_largest(array))
    