import java.util.*;
public class Day4 {
    public static void main(String[] args) {
        // factorial
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number : ");
        int num = input.nextInt();
        int factorial = num * (num-1);
        for (int i = 2; i<num; i++){
            factorial = factorial * (num-i);
        }
        System.out.println(factorial);
        input.close();
    }
}
