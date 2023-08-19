#include <stdio.h>
void main(){
    int arr[] = {10,20,30,40,50,60};
    int max = arr[0];
    int secondMax = arr[0];
    for (int i = 1; i < sizeof(arr); i++)
    {
        if (arr[i]>max)
        {
            secondMax = max;
            max = arr[i];
        }
    }
    printf("%d",secondMax);
}