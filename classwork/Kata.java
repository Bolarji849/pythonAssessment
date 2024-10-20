import java.util.Scanner;
public class Kata{

	public static void main (String[] args){
	Scanner numbercollection = new Scanner(System.in);
	System.out.println("Enter number");
	int userinput = numbercollection.nextInt();

	System.out.print(primeNumber(userinput));




}
   



 	public static boolean evenNumbers(int number){
 	if(number%2 == 0){
         return true ;
	 }
	 return false;
	 }


	public static boolean primeNumber(int number)
 	for(counter = 0;counter < number; counter++){
	  int factor = 1;

	   if(number % factor == 0) digit++
		if(factor == 2){
		 return true
		}
		return false
	}








}