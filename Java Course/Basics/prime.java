import java.util.Scanner;

public class prime {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // condition for prime numbers -- method 1
        System.out.print("Enter the number : ");
        int num = input.nextInt();
        boolean check = false;
        for (int i=2; i<=num/2;i++){
            if(num % i == 0){
                check = true;
                break;
            }
        }
        if (check == false){
            System.out.println("It is prime");
        }
        else{
            System.out.println("It is not a prime");
        }

        
        // condition for prime -- method 2
        System.out.print("Enter the number : ");
        int number = input.nextInt();
        int factor = 0;
        for (int i=2; i<=number; i++){
            if(number%i == 0){
                factor++;
            }
        }
        if(factor==1){
            System.out.println("It is prime");
        }
        else{
            System.out.println("It is not prime");

        }

        input.close();
    }
}
