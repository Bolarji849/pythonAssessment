def main_menu():
		main_menu = print("""  
		Main Menu   
		1 >>  Phonebook	
			2 >>  Messages
			3 >>  Chat		
			4 >>  Call register
			5 >>  Tone
			6 >>  Settings
			7 >>  Call divert
			8 >>  Games
			9 >>  Caculator
			10 >> Reminders
			11 >> Clock
			12 >> Profiles
			13 >> Sim services
			0>> Exit	
			""") 

		response  = int(input("Enter Number"))

		match response:
			case 0:
				print("Thank You For Using Our app")
			case 1:
				phone_book()
				main_menu()
			case 2:
				message()
				main_menu()	
			case 3:
				chat()
				main_menu()
			case 4:
				call_register()
				main_menu()
			case 5:
				tones()
				main_menu()
			case 6:
				settings()
				main_menu()
			case 7:
				call_divert()
				main_menu()
			case 8:
				games()
				main_menu()
			case 9:
				calculator()
				main_menu()
			case 10:
				reminder()
				main_menu()
			case 11:
				clock()
				main_menu()
			case 12:
				profiles()
				main_menu()
			case 13:
				sim_services()
				main_menu()
			case 0:
				main_menu()


def phone_book():
	print("""
    			.......................
			Phone book menu
    			1 >>  Search
    			2 >>  Service Nos
    			3 >>  Add name
    			4 >>  Erase
    			5 >>  Edit
    			6 >>  Assign tone
    			7 >>  Send b'card	 			
    			8 >>  Options
    			9 >>  Speed dials
    			10 >> Voice tags
			11 >> Back To Main Menu
    			......................	
	""") 
	Phonebook_menu = int(input("Please enter number: "))
	
	match Phonebook_menu:
		case 1:
			print("Search")
			phone_book_inner_method()
		case 2:
			print("Service Nos")
			phone_book_inner_method()
		case 3:
			print("Add name")
			phone_book_inner_method()
		case 4:
			print("Erase")	
			phone_book_inner_method()
		case 5:
			print("Edit")	
			phone_book_inner_method()
		case 6:
			print("Assign tone")
			phone_book_inner_method()
		case 7:
			print("Send b' card")
			phone_book_inner_method()
		case 8:
			print("""
			      1. Type of view
                              2. Memory status    
						
						""")
			option_menu = int(input("Please enter number: "))
			match option_menu:
				case 1:
					print("Type of view")
					phone_book_inner_method()
					
				case 2:
					print(" Memory status ")
					phone_book_inner_method()
		case 9:
			print("Speed dials")
			phone_book_inner_method()
		case 10:
			print("Voice tags")
			phone_book_inner_method()
		case 11:
			main_menu()



def phone_book_inner_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		phone_book()

def message():
	print("""
    			.......................
			Message menu
    			1 >>  Write messages
    			2 >>  Inbox
    			3 >>  Outbox
    			4 >>  Picture messages
    			5 >>  Templates
    			6 >>  Smileys
    			7 >>  Message settings 			
    			8 >>  Info service
			9. Voice mailbox number
			10.Service command editor
    			......................	
	""") 
	message_menu = int(input("Please enter number: "))
	
	match message_menu:
		case 1:
			print("Write messages")
			message_menu_method()
		case 2:
			print("Inbox")
			message_menu_method()
		case 3:
			print("Outbox")
			message_menu_method()
		case 4:
			print("Picture messages")
			message_menu_method()
		case 5:
			print("Templates")
			message_menu_method()
		case 6:
			print(" Smileys")
			message_menu_method()
		case 7:
			print("""
				1.Set
				  
				
				2. Common
					""")
			message_settings_menu = int(input("Please enter number: "))
			match message_settings_menu:
					case 1:
						print("""
							1. Message centre number
							2. Messages sent as
							3. Message validity	
							""")
					case 2:
						print("""
							1.Delivery reports
							2. Reply via same centre
							3. Character support
							""")
						set_menu = int(input("Please enter number: "))
						match set_menu:
							case 1:
								print("Message centre number")
							case 2:
								print("Messages sent as")
							case 3:
								print("Message validity")
								message_menu_method()
											
								set_menu = int(input("Please enter number: "))
								match Common_menu:
									case 1:	
										print("Delivery reports")
									case 2:
									  	print("Reply via same centre")	
									case 3:
										print("Character support")
										message_menu_method()
		case 8:		
			print("Info service")
			message_menu_method()
		case 9:
			print("Voice mailbox number")	
			message_menu_method()			
		case 10:
			print("Service command editor")
			message_menu_method()
		
			


def message_menu_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		message()




def chat():
	print("""
    			.......................
				Chat
    			1 >>  Chat
    			
			0 >> Back To Main Menu
    			......................	
	""") 
	chat_menu = int(input("Please enter number: "))
	match chat_menu:
		case 1:
			print(" Chat ")
			main_menu()
			
		case 0:
			 main_menu()
			


def call_register():
	print("""
    			.......................
			Call register menu
    			1 >>  Missed calls
    			2 >>  Received calls
    			3 >>  Dialled numbers
    			4 >>  Erase recent call lists
    			5 >>  Show call duration
    			6 >>  Show call costs
    			7 >>  Call cost settings	 			
    			8 >>  Prepaid credit
			0 >> Back To Main Menu
    			......................	
	""") 
	Call_register_menu = int(input("Please enter number: "))
	match Call_register_menu:
		case 1:
			print("Missed calls")
			call_register()
		case 2:
			print("Received calls")
			call_register()
		case 3:
			print("Dialled numbers")
			call_register()
		case 4:
			print("Erase recent call lists")	
			call_register()
		case 5:
			print(""" 
				1. Last call duration
				2. All calls’ duration
				3. Received calls’ duration
				4. Dialled calls’ duration
				5. Clear timers
				

				""")	
			show_call_duration_menu = int(input("Please enter number: "))
			match show_call_duration_menu:
					case 1:	
						print("Last call duration")
						call_register()
					case 2:
						print(" All calls’ duration")
						call_register()	
					case 3:
						print("Received calls’ duration")
						call_register()
					case 4:
						print("Dialled calls’ duration")
						call_register()
					case 5:
						print("Clear timers")
						call_register()

			
		case 6:
			print(""" 
				1. Last call cost
				2. All calls’ cost
				3. Clear counters
				""")


			show_call_costs_menu = int(input("Please enter number: "))
			match show_call_costs_menu:
					case 1:
						print("Last call cost")
						Call_register_menu_method()
					case 2:
						print("All calls’ cost")
						Call_register_menu_method()
					case 3:
						print("Clear counters")
						Call_register_menu_method()
			
		case 7:
			print("""            
				1. Call cost limit
				2. Show costs in

				""")
			call_cost_settings_menu = int(input("Please enter number: "))
			match call_cost_settings_menu:
					case 1:
						print("Call cost limit")
						Call_register_menu_method()
					case 2:
						print("Show costs in")
						Call_register_menu_method()
					
			
		case 8:
			print("Prepaid credit")
			Call_register_menu_method()




def Call_register_menu_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		call_register()




def tones():
	print("""
    			.......................
			Tones menu
    			1 >> Ringing tone
    			2 >> Ringing volume
    			3 >> Incoming call alert
    			4 >> Composer
    			5 >> Message alert tone
    			6 >> Keypad tones
    			7 >> Warning and game tones	 			
    			8 >> Vibrating alert
			9 >> Screen saver
			0 >> Back To Main Menu
    			......................	
	""") 
	tones_menu = int(input("Please enter number: "))
	match tones_menu:
		case 1:
			print("Ringing tone")
			tones_menu_method()
			
		case 2:
			print("Ringing volumes")
			tones_menu_method()
			
		case 3:
			print("Incoming call alerts")
			tones_menu_method()
			
		case 4:
			print(" Composer")
			tones_menu_method()
		case 5:
			print("Message alert tone")
			tones_menu_method()
		case 6:
			print("Keypad tones")
			tones_menu_method()	
		case 7:
			print("Warning and game tones")
			tones_menu_method()
		case 8:
			print("Vibrating alert")
			tones_menu_method()
		case 9:
			print("Screen saver")
			tones_menu_method()
		case 0:
			tones_menu_method()
			
			

def tones_menu_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		tones()




def settings():
	print("""
    			.......................
			Settings menu
    			1 >> Call settings
    			2 >> Phone settings
    			3 >> Security settings
    			4 >> Restore factory settings
			0 >> Back To Main Menu
    			......................	
	""") 
	

	settings_menu = int(input("Please enter number: "))
	match settings_menu:
		case 1:
			print("""
				1. Automatic redial
				2. Speed dialling
				3. Call waiting options
				4. Own number sending
				5. Phone line in use
				6. Automatic answer
			""")
			call_settings_menu = int(input("Please enter number: "))
			match call_settings_menu:
					case 1:
						print("Automatic redial")
						settings_menu_method()
					case 2:
						print("Speed dialling")
						settings_menu_method()
					case 3:
						print("Call waiting options")
						settings_menu_method()
					case 4:
						print("Own number sending")
						settings_menu_method()
					case 5:
						print("Phone line in use")
						settings_menu_method()
					case 6:
						print("Automatic answer")
						settings_menu_method()

			
			
		case 2:
			print("""
				1. Language
				2. Cell info display
				3. Welcome note
				4. Network selection
				5. Lights 
				6. Confirm SIM service actions
			""")
			
			phone_settings_menu = int(input("Please enter number: "))
			match phone_settings_menu:
					case 1:
						print("Language")
						settings_menu_method()
					case 2:
						print("Cell info display")
						settings_menu_method()
					case 3:
						print("Welcome note")
						settings_menu_method()
					case 4:
						print("Network selection")
						settings_menu_method()
					case 5:
						print("Lights ")
						settings_menu_method()
					case 6:
						print("Confirm SIM service actions")
						settings_menu_method()




		case 3:
			print("""
				1. PIN code request
				2. Call barring service
				3. Fixed dialling
				4. Closed user group
				5. Phone security
				6. Change access codes
			""")


			Security_settings_menu = int(input("Please enter number: "))
			match Security_settings_menu:
					case 1:
						print("PIN code request")
						settings_menu_method()
					case 2:
						print("Call barring service")
						settings_menu_method()
					case 3:
						print("Fixed dialling")
						settings_menu_method()
					case 4:
						print("Closed user group")
						settings_menu_method()
					case 5:
						print("Phone security")
						settings_menu_method()
					case 6:
						print("Change access codes")
						settings_menu_method()

		case 4:
			print("Restore factory settings")
			settings_menu_method()

	

def settings_menu_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		settings()

def call_divert():
	print("""
    			.......................
			Call divert Menu
    			1 >>  Call divert
			0 >> Back To Main Menu
    			......................	
	""") 
	call_divert_menu = int(input("Please enter number: "))
	
	match call_divert_menu:
		case 1:
			print("Call diver")
			main_menu()
			
		case 0:
			main_menu()

def games():
	print("""
    			.......................
			    Games Menu
    			1 >>  Games
			0 >> Back To Main Menu
    			......................	
	""") 
	games_menu = int(input("Please enter number: "))
	
	match games_menu:
		case 1:
			print("Games")
			main_menu()
			
		case 0:
			main_menu()



def Calculator():
	print("""
    			.......................
			  Calculator Menu
    			1 >> Calculator
			0 >> Back To Main Menu
    			......................	
	""") 
	calculator_menu = int(input("Please enter number: "))
	
	match calculator_menu:
		case 1:
			print("Calculator")
			main_menu()
			
		case 0:
			main_menu()




def reminder():
	print("""
    			.......................
			    Reminder Menu
    			1 >> Reminders
			0 >> Back To Main Menu
    			......................	
	""") 
	reminder_menu = int(input("Please enter number: "))
	
	match reminder_menu:
		case 1:
			print("Reminders")
			main_menu()
			
		case 0:
			main_menu()



def clock():
	print("""
    			.......................
			Clock menu
    			1 >>  Alarm clock
    			2 >>  Clock settings
    			3 >>  Date setting
    			4 >>  Stopwatch
    			5 >>  Countdown timer
    			6 >>  Auto update of date and time
			0 >> Back To Main Menu
    			......................	
	""") 
	clock_menu = int(input("Please enter number: "))
	
	match clock_menu:
		case 1:
			print("Alarm clock")
			clock_menu_method()
		case 2:
			print("Clock settings")
			clock_menu_method()
		case 3:
			print("Date setting")
			clock_menu_method()
		case 4:
			print("Stopwatch")
			clock_menu_method()
		case 5:
			print("Countdown timer")
			clock_menu_method()
		case 6:
			print("Auto update of date and time")
			clock_menu_method()
		case 0:
			main_menu()
			


def clock_menu_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		clock()	


	
def profiles():
	print("""
    			.......................
			    Profile_Menu
    			1 >>  Profiles
			0 >> Back To Main Menu
    			......................	
	""") 
	profile_menu = int(input("Please enter number: "))
	
	match profile_menu:
		case 1:
			print("Profiles")
			main_menu()
			
		case 0:
			main_menu()



def  sim_services():
	print("""
    			.......................
			   SIM services
    			1 >>  SIM services
			0 >> Back To Main Menu
    			......................	
	""") 
	sim_services_menu = int(input("Please enter number: "))
	match sim_services_menu:
		case 1:
			print("SIm services")
			main_menu()
		case 0:
			main_menu()

		

			





		
		













		


main_menu()
		
	
        

		
		
		
		

		




       


