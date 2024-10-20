import java.util.Scanner;
public class NokiaBackFunction{

	public static void main(String[] args){
	
	String prompt = """  
			Main Menu   
			1 >>  Phone book	
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
				
					"""; 
				
	System.out.print(prompt);
	Scanner input = new Scanner(System.in);

        System.out.print(" Please Enter Option ");
	int userInput = input.nextInt();

         DisplayMenu(userInput);



      
	switch (userInput ){
	case 1: System.out.print("""

				   >>>>>Phone book menu<<<<<
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
							  """); 
		
	
        
        System.out.print(" Please Enter Option   ");
				
	int phoneBook = input.nextInt();
	DisplayMenu(userInput);
	switch (phoneBook){
		case 1: System.out.print(" Search "); break;
		case 2: System.out.print(" Service Nos ");break;
		case 3: System.out.print("  Add name ");break;
		case 4: System.out.print("  Erase ");break;
		case 5: System.out.print("  Edit  ");break;
		case 6: System.out.print(" Assign tone ");break;
		case 7: System.out.print(" Send b'card ");break;
	        case 8: System.out.print(""" 
							Options
						1 >> Type of view
						1 >> Memory status									
							            """);



        System.out.print(" Please Enter Option   ");
	int Options = input.nextInt();
	switch (Options){
	  case 1: System.out.print(" Type of view ");break;
	  case 2: System.out.print(" Memory status ");break;
	  }
	               break;
	  case 9: System.out.print("Speed dials ");break;
	  case 10: System.out.print(" Voice tags ");break;
          




	


	public static void DisplayMenu(){

		for( i = 0; i > numberEntered; i++){
		if( numberEntered == 0)
                 System.out.print(prompt);
                }
                }









}
}  