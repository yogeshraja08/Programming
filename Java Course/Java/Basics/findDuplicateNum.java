import java.util.Scanner;

public class findDuplicateNum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the size of array : ");
        int size = input.nextInt();
        int[] arr = new int[size];
        for (int i=0; i<size; i++){
            System.out.print("Enter the value : ");
            int val = input.nextInt();
            arr[i]=val;
        }
        int count=0;
        for (int j=0; j<size; j++){
            for (int k=j+1; k<size; k++){
                if(arr[j] == arr[k]){
                    System.out.print(arr[k]+" ");
                    count++;
                }
            }
        }
        System.out.println("\nTotal no. of duplicated numbers : "+count);
        input.close();
    }
}
