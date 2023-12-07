import java.util.Scanner;

public class primeSum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // condition for sum of prime numbers
        System.out.print("Enter the starting number : ");
        int a = input.nextInt();
        System.out.print("Enter the ending number : ");
        int b = input.nextInt();
        int primesum = 0;
        for(int j=a; j<=b; j++)
        {   
            int num = j;
            int factor = 0;
            for (int i=2; i<=num;i++){
                if(num%i==0){
                    factor++;
                }
            }
            if (factor==1){
                primesum+=j;
            }
        }
        System.out.println(primesum);

        input.close();
    }
}
