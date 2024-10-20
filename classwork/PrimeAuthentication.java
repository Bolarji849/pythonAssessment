import java.util.Scanner;
public class PrimeAuthentication{
public static void main(String[] args){

	Scanner numbercollection = new Scanner(System.in);
	System.out.print("Enter a number");
	int number = numbercollection.nextInput();

        
        int factors = 0;
	for(int digit = 1; digit < number;digit++){
		if(number % digit ==0) factors++;
                 
               }      
		if (factors == 2)
		System.out.print(number+"is a prime number");
		else
                System.out.print("it's not a prime number");
  		

         









}








}