#include <stdio.h>
void main(){
    int arr[] = {10,20,30,40,50,66,77,88,99};
    int search,count=0;
    printf("Enter the number to be found : ");
    scanf("%d",&search);
    for (int i = 0; i < sizeof(arr); i++)
    {
        if (search == arr[i])
        {
            count++;
        }
    }
    if (count>0)
    {
        printf("The number is found at %d times",count);
    }
    else
    {
        printf("The number doesn't found");
    }
}