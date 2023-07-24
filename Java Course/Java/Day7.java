import java.util.Scanner;

public class Day7 {
    public static void main(String[] args) {
        // Scanner input=new Scanner(System.in);
        // System.out.print("Enter the Size of array : ");
        // int size = input.nextInt();
        // int[] arr = new int[size];
        // // int sum = 0;
        // for (int i=0; i<size; i++){
        //     System.out.print("enter the "+i+"th index : ");
        //     arr[i] = input.nextInt();
        // }
        // // for(int j=0; j<size; j++){
        // //     sum+=arr[j];
        // // }
        // // System.out.println("Sum : "+sum);
        
        // // // int arr[] = {8,5,3,2,6,9,1,4};
        // // int min = arr[0];
        // // for (int i=1; i<arr.length; i++){
        // //     if (min>arr[i]){
        // //         min = arr[i];
        // //     }
        // // }
        // // int max = arr[0];
        // // for (int i=1; i<arr.length; i++){
        // //     if (max<arr[i]){
        // //         max = arr[i];
        // //     }
        // // }
        // // System.out.println("Min : "+min);
        // // System.out.println("Max : "+max);

        // for (int i=0; i<arr.length;i++){
        //     for (int j=i+1; j<arr.length;j++){
        //         if(arr[i]<arr[j]){
        //             int temp = arr[i];
        //             arr[i] = arr[j];
        //             arr[j] = temp;
        //             temp = 0;
        //         }
        //     }
        // }
        // for (int i=0; i<arr.length;i++){
        //     if(arr[i]%2==0){
        //         System.out.print(arr[i]+" ");
        //     }
        // }
        // input.close();

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
            if (arr[j]%2 == 0){
                sum += arr[j];
            }
        }
        System.out.println(sum);
        input.close();
    }
}
