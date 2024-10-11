investment_amount = int(input("ENTER INVESTMENT AMOUNT:"))
percentage = int(input("ENTER PERCENTAGE RATE:"))
number_of_years = int(input("ENTER NUMBER OF YEARS:"))
if not isinstance(investment_amount,int):
	raise valueError("invaild input")
if investment_amount < 0:
	print("invaild input")
if percentage < 0:
	print("invaild input")
if number_of_years < 0:
	print("invaild input")




total = 0
print("YEAR "        "    ROI   "        "   AMOUNT ")

for roi in range(1,number_of_years+1):
	return_on_investment =  investment_amount / 100 * percentage 
	total = investment_amount + return_on_investment
	print(f"{roi}     {investment_amount:,.2f}  {total:,.2f}")
	investment_amount = total


