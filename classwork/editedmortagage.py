
principal  = float (input("Enter Principal "))
rate	   = float (input("Enter rate "))
duration_of_years = float (input("Enter number of Duration in years  "))	




	
monthly_interest_rate = (rate/100)/12
       
number_of_in_a_year = duration_of_years * 12
'''	
raise_to_power = (1+percentage_rate**number_of_in_a_year)
	
caculate_numinator = percentage_rate * raise_to_power
	
calculate_denuminator = raise_to_power - 1
'''

monthly_payment = principal * (monthly_interest_rate * 1 + monthly_interest_rate) **number_of_in_a_year \
/(1+monthly_interest_rate )**number_of_in_a_year -1

print( "Your mothly payment  is ",monthly_payment)



''' prompt user to enter principal amount 
    prompt user to enter rate
    prompt user to duration of years
    mutiply duration of years by numbers of month in a year
	calculate using the formulate given
	display the result '''