import java.util.Scanner;

public class pattens {
    public static void main(String[] args) {
        // pattens
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the range : ");
        int range = input.nextInt();
        for (int i=range; i>=0; i--){
            for (int j=0; j<i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        input.close();
    }
}
