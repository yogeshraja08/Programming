import java.util.Scanner;

public class compareNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number 1 : ");
        int num1 = input.nextInt();
        System.out.print("Enter the number 2 : ");
        int num2 = input.nextInt();
        System.out.print("Enter the number 3 : ");
        int num3 = input.nextInt();

        if ((num1>num2) && (num1>num3)){
            System.out.println("Number 1 is biggest number");
        }
        else if ((num1<num2) && (num1<num3)){
            System.out.println("Number 1 is smallest number");
        }
        else if ((num1 == num2) || (num2 == num3)){
            System.out.println("Two of the given numbers are same");
        }
        else{
            System.out.println("number 1 is "+num1);
            System.out.println("number 2 is "+num2);
            System.out.println("number 3 is "+num3);
        }
        input.close();
    }
}
