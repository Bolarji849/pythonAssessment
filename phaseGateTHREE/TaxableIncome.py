
print('''
	single Tax - 1
	………………………………………………..
	
	married_joint_Tax -2 
	……………………………………………………….
	married_seprately - 3
	………………………………………………………..
	head_household_tax - 4
	……………………………………………………………..
				''')


userInput =  int(input("Enter menu number "))

Taxable_amount = int(input("Enter Taxable amount "))

balance = 0
if( userInput ==1):
	if(Taxable_amount > 0 and Taxable_amount <= 8350):
		balance = Taxable_amount * 0.10
		print(balance)

	if(Taxable_amount > 8351 and Taxable_amount <= 33950):
		balance =  (8350 * 0.10 ) + (Taxable_amount - 8350)*0.15
		print(balance)


	if(Taxable_amount > 33951 and Taxable_amount <= 82250):
		balance =  (8350 * 0.10 ) + (33950 - 8350) *0.15 + (Taxable_amount - 33950)*0.25
		print(balance)
	if(Taxable_amount >82251 and Taxable_amount <= 171550):
		balance =  (8350 * 0.10 ) + (33950 - 8350) *0.15 + (82250 -33950)*0.25 +(Taxable_amount - 82250 )*0.28
		print(balance)
	if(Taxable_amount >171551 and Taxable_amount <= 372950):
		balance =  (8350 * 0.10 ) + (33950 - 8350) *0.15 + (82250 -33950)*0.25 +( 171550 - 82250 )*0.28 +(Taxable_amount - 171550 )* 0.33
		print(balance)
	if(Taxable_amount >372951):
		balance =  (8350 * 0.10 ) + (33950 - 8350) *0.15 + (82250 -33950)*0.25 +( 171550 - 82250 )*0.28 +(372950 - 171550 )* 0.33 + (Taxable_amount - 372950)*0.35
		print(balance)



if( userInput ==2):
	if(Taxable_amount > 0 and Taxable_amount <= 16700):
		balance = Taxable_amount * 0.10
		print(balance)

	if(Taxable_amount >16701 and Taxable_amount <= 67900):
		balance =  (16700 * 0.10 ) + (Taxable_amount - 16700)*0.15
		print(balance)


	if(Taxable_amount > 67901 and Taxable_amount <= 137050):
		balance =  (16700* 0.10 ) + (67900 - 16700) *0.15 + (Taxable_amount - 67900)*0.25
		print(balance)

	if(Taxable_amount >137051 and Taxable_amount <= 208850):
		balance =  (16700 * 0.10 ) + (67900- 16700) *0.15 + (137050 -67900)*0.25 +(Taxable_amount - 137050 )*0.28
		print(balance)

	if(Taxable_amount >208,851 and Taxable_amount <= 372950):
		balance =  (16700 * 0.10 ) + (67900 - 16700) *0.15 + (137050 -67900)*0.25 +( 208850 - 137050 )*0.28 +(Taxable_amount - 208850 )* 0.33
		print(balance)
	if(Taxable_amount >372951):
		balance =  (16700 * 0.10 ) + (67900 -  16700) *0.15 + (137050-67900)*0.25 +( 208850 - 137050 )*0.28 +(372950 - 208850 )* 0.33 + (Taxable_amount - 208850)*0.35
		print(balance)


if( userInput ==3):
	if(Taxable_amount > 0 and Taxable_amount <= 8350):
		balance = Taxable_amount * 0.10
		print(balance)

	if(Taxable_amount >8351 and Taxable_amount <= 33950):
		balance =  (8350* 0.10 ) + (Taxable_amount - 8350)*0.15
		print(balance)


	if(Taxable_amount > 33951 and Taxable_amount <= 68525):
		balance =  (8350 * 0.10 ) + (33950 - 8350) *0.15 + (Taxable_amount - 33950)*0.25
		print(balance)

	if(Taxable_amount >68526 and Taxable_amount <= 104425):
		balance =  (8350  * 0.10 ) + (33950 - 8350) *0.15 + (68525 -33950)*0.25 +(Taxable_amount - 68525)*0.28
		print(balance)

	if(Taxable_amount >104426 and Taxable_amount <= 186475):
		balance =  (8350 * 0.10 ) + (33950 - 8350) *0.15 + (68525 -33950)*0.25 +( 104425 - 68525)*0.28 +(Taxable_amount - 104425 )* 0.33
		print(balance)
	if(Taxable_amount >186476):
		balance =  (8350 * 0.10 ) + (33950  -  8350) *0.15 + (68525-33950)*0.25 +( 104425  - 68525 )*0.28 +(186475 - 104425 )* 0.33 + (Taxable_amount - 186475)*0.35
		print(balance)


if( userInput ==4):
	if(Taxable_amount > 0 and Taxable_amount <= 11950):
		balance = Taxable_amount * 0.10
		print(balance)

	if(Taxable_amount >11951 and Taxable_amount <= 45500):
		balance =  (11950* 0.10 ) + (Taxable_amount - 11950)*0.15
		print(balance)


	if(Taxable_amount > 45501 and Taxable_amount <= 117450):
		balance =  (11950 * 0.10 ) + (45500 - 11950) *0.15 + (Taxable_amount - 45500)*0.25
		print(balance)

	if(Taxable_amount >117451 and Taxable_amount <= 190200):
		balance =  (11950 * 0.10 ) + (45500 - 11950) *0.15 + (117450 -45500)*0.25 +(Taxable_amount - 117450)*0.28
		print(balance)

	if(Taxable_amount >190201 and Taxable_amount <= 372950):
		balance =  (11950 * 0.10 ) + (45500  - 11950) *0.15 + (117450 -45500)*0.25 +( 190200 - 117450)*0.28 +(Taxable_amount - 190200 )* 0.33
		print(balance)
	if(Taxable_amount >372951):
		balance =  (11950 * 0.10 ) + (45500   -  11950) *0.15 + (117450 -45500)*0.25 +( 190200  - 117450 )*0.28 +(372950 - 190200  )* 0.33 + (Taxable_amount - 372950)*0.35
		print(balance)








