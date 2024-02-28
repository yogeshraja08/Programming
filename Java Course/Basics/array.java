import java.util.Scanner;

public class array {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the Size of array : ");
        int size = input.nextInt();
        int[] arr = new int[size];
        int sum = 0;
        for (int i=0; i<size; i++){
            System.out.print("enter the "+i+"th index : ");
            arr[i] = input.nextInt();
        }
        for(int j=0; j<size; j++){
            sum+=arr[j];
        }
        System.out.println("Sum : "+sum);
        input.close();
    }
}
