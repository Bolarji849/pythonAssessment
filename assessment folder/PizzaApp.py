
			
	

def caculate_size_of_pizza(snumberOfPeople,numberOfSlice,prices):
	
	sliceRemainder = 0
	numberOfPacks = numberOfPeople/numberOfSlice
	numberOfPacks = numberOfPeople/numberOfSlice
	if(numberOfPeople % numberOfSlice != 0):
		numberOfPacks = numberOfPacks+1;
	sliceRemainder = numberOfPacks*numberOfSlice - numberOfPeople
	price = numberOfPacks*price
	print(f"Number of boxes of pizza is {int(number_of_packs)})
	print(f"Number Of left over slice after serving:{sliceRemainder})
	print(f"price is  { price:.2f }" )
		











 print("""
			.................................................
			Pizza type    Number of Slices    Price per box
			.................................................
			1.) Sapa size            4                 2,000

			2.) Small Money          6                 2,400

			3.) Big boys             8                 3,000

			4.) Odogwu              12                 4,200
			................................................


								""")
print(menu)
pizzaType = int(input("Enter number for type of pizza")) 
numberOfPeople = int(input("Enter the amount of people you're hosting"))
	





match(pizzaType):
	case 1:
		caculate_size_of_pizza(numberOfPeople, 4, 2000.00)
	case 2: 
		caculate_size_of_pizza(numberOfPeople, 6, 2400.00)
	case 3: 
		caculate_size_of_pizza(numberOfPeople, 8, 3000.00)
	case 4: 
		caculate_size_of_pizza(numberOfPeople, 12, 4200.00)
	case _:
		print("You have enter wrong input good bye ")






