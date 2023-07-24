import java.util.Scanner;

public class Day7 {
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
        
        // int arr[] = {8,5,3,2,6,9,1,4};
        int min = arr[0];
        for (int i=1; i<arr.length; i++){
            if (min>arr[i]){
                min = arr[i];
            }
        }
        int max = arr[0];
        for (int i=1; i<arr.length; i++){
            if (max<arr[i]){
                max = arr[i];
            }
        }
        System.out.println("Min : "+min);
        System.out.println("Max : "+max);
        input.close();
    }
}
