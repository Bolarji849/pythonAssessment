
"""
write a python program to read a number from the command prompt and print a right triangle using"*"

sample input : 5

sample output
"""
user_input = int(input('Sample output: '))
for number in range(1, 11):
    print (user_input ,'*', number ,'=', user_input * number)