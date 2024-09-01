delivery_amount = int(input("Enter amount of successful delivery"))

def caculateLogistics():
	BASEPAY = 5000
		

	if(delivery_amount >= 70):
		amount_per_percel = 500
		result = delivery_amount*amount_per_percel+BASEPAY
		print("your wage for the day is  " , result)
	
			
	elif(delivery_amount>=60 and delivery_amount <= 69):
		amount_per_percel = 250
		result = delivery_amount*amount_per_percel+BASEPAY
		print("your wage for the day is  " , result )
			
		 
	elif(delivery_amount>=50 and delivery_amount <= 59):
		amount_per_percel = 200
		result = delivery_amount*amount_per_percel+BASEPAY
		print("your wage for the day is  " , result)
		      
		
	else: 
		     	
		amount_per_percel = 160
		result = (delivery_amount*amount_per_percel)+BASEPAY
		print("your wage for the day is  ", result  )
			
			
		

caculateLogistics()


		




