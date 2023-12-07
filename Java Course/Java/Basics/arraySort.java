public class arraySort {
    public static void main(String[] args) {
        int arr[] = {8,5,3,2,6,9,1,4};
        for (int i=0; i<arr.length;i++){
            for (int j=i+1; j<arr.length;j++){
                if(arr[i]<arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                    temp = 0;
                }
            }
        }
        for (int i=0; i<arr.length;i++){
            if(arr[i]%2==0){
                System.out.print(arr[i]+" ");
            }
        }
    }
}
