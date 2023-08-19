#include <stdio.h>
void main(){
    int arr[] = {10,20,30,27,62,55,84,72};
    int min,max;
    min=arr[0];
    max=arr[0];
    for (int i = 1; i<8; i++)
    {
        if (min > arr[i])
        {
            min = arr[i];
        }
        if (max < arr[i])
        {
            max = arr[i];
        }
    }
    printf("The minimum value in the array is %d",min);
    printf("\nThe maxmium value in the array is %d",max);
}