import java.util.Scanner;

public class SumEvenOdd_range {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter start number : ");
        int a = input.nextInt();
        System.out.print("Enter end number : ");
        int b = input.nextInt();
        int sum=0, evenSum=0, oddSum=0;
        for(int i = a;i<=b;i++){
            if(i%2==0){
                evenSum+=i;
            }
            else{
                oddSum+=i;
            }
            sum+=i;
        }
        System.out.println("Sum of the total numbers is "+sum);
        System.out.println("Sum of the even numbers is "+evenSum);
        System.out.println("Sum of the odd numbers is "+oddSum);

        input.close();
    }
}
