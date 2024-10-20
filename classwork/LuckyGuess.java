import java.util.Scanner;
import java.security.SecureRandom;
public class LuckyNumberGuess {

	public static void main(String[] args){


	Scanner inuputnumber = new Scanner(System.in);
	SecureRandom random = new SecureRandom();

	int randomNumber = random.nextInt(1,10);




	int guessNumber = 0;
	
	int counter = 1;




	while (guessNumber != randomNumber){
		System.out.print(" guess what the number is  ");
		 guessNumber = inuputnumber.nextInt();
	   while( counter <= 3){
			counter++;
			}
		if ( guessNumber > randomNumber){
			System.out.println("Too high, try again");
		}
		if ( guessNumber < randomNumber){
			System.out.println("Too low, try again");
		}
		if ( guessNumber ==  randomNumber){
			System.out.println("Correct great job you finally got the answer"); }
		
		}


	}




	}