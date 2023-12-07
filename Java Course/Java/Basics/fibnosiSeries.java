import java.util.Scanner;

public class fibnosiSeries {
    public static void main(String[] args) {
        // fibnosi serious
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the range : ");
        int num = input.nextInt();
        int n1=0,n2=1;
        System.out.print(n1 + " " + n2 + " ");
        for (int i=1; i<num;i++){
            int n3 = n1 + n2;
            System.out.print(n3+" ");
            n1 = n2;
            n2 = n3;
        }
        input.close();
    }
}
