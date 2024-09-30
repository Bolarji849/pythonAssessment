userinput = int(input("Enter today's day: "))

sunday = 0
monday = 1
tuesday = 2
wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6

match userinput:
		case 1:
			print("Today is monday")
		case 2:
			print("Today is Tuesday ")
		case 3:
			print("Today is  Wednesday ")
		case 4:
			print("Today is  Thursday ")
		case 5:
			print("Today is  Friday")
		case 6:
			print("Today is  Saturday ")
		case 0:
			print("Today is  Sunday ")

future_day = int(input("Enter number of days elapsed: "))
total = future_day + userinput
match total:
		case 1:
			print(" future is monday")
		case 2:
			print("future is Tuesday ")
		case 3:
			print("future is  Wednesday ")
		case 4:
			print("future is  Thursday ")
		case 5:
			print("future is  Friday")
		case 6:
			print("futre is  Saturday ")
		case 0:
			print("future is  Sunday ")

				