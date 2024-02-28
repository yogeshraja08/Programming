import java.util.Scanner;

public class evenOdd {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number : ");
        int a = input.nextInt();
        //datatype var = (condition) ? true:false;
        String evenOdd = ((((a%2==0) || (a==10)) && a>0) ? "even":"odd" );
        System.out.println(evenOdd);
        input.close();
    }
}
