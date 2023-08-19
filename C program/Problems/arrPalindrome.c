#include <stdio.h>
void main(){
    int size;
    printf("Enter the size of array : ");
    scanf("%d",&size);
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        printf("Enter the value of %d index : ",i);
        scanf("%d",&arr[i]);
    }
    int i=0,j=size-1,flag=0;
    while(i<j){
        if(arr[i]!=arr[j]){
            flag=1;
        }
        i++;
        j--;
    }
    if (flag==0)
    {
        printf("It is a palindrome");
    }
    else{
        printf("It is not a palindrome");
    }
}