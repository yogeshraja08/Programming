import java.util.Scanner;

public class arraySum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the size of array : ");
        int size = input.nextInt();
        int[] arr = new int[size];
        for (int i=0; i<size; i++){
            System.out.print("Enter the val : ");
            int val = input.nextInt();
            arr[i]=val;
        }
        int sum = 0;
        for (int j=0; j<size; j++){
            sum += arr[j];
        }
        System.out.println(sum);
        input.close();
    }
}
