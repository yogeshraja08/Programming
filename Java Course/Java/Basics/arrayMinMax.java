public class arrayMinMax {
    public static void main(String[] args) {
        int arr[] = {8,5,3,2,6,9,1,4};
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
    }
}
