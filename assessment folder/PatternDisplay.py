def pattern_display(number):
    reverse = 0
    while number != 0:
        reverse = reverse * 10 + number % 10
        number = number / 10
    print(reverse)

def main():
    number = int(input("Enter the number: "))
    pattern_display(number)


    main()