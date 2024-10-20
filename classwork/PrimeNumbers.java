import java.util.Scanner;
public class Primevalidator{
public static void main(String[] args){

	Scanner numbercollection = new Scanner(System.in);
	System.out.print("Enter a number");
	int number = numbercollection.nextInput();

        

	for(int digit = 2; digit < number;digit++){
		if(number % digit ==0)
                    System.out.print("it's not a prime number")
                     
		
		System.out.print(" it's a prime number");
                 
  		

         }









}








}