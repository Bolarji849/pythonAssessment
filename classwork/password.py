'''
request password from user
store as password
get the length of the password
display in astericks

'''


password = input("Enter password: ")
password_count = len(password)
astericks = '*'
password= password_count*astericks
print(password)