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
			case _:
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
    			5 >>  Edit
    			6 >>  Templates
    			7 >>  Smileys	 			
    			8 >>  Message settings
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
								
			


def message_menu_method():
	response = int(input("Enter 0 to go back to previous page or -1 "))
	if response == -1:
		main_menu()
	else:
		message()

		


main_menu()
		
	
        

		
		
		
		

		




       


