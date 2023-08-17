#include<stdio.h>

void main(){
    int num;
    printf("Enter the number : ");
    scanf("%d",&num);
    int rev=0;
    while (num>0)
    {
        rev = rev * 10 + (num%10);
        num = num / 10;
    }
    printf("%d",rev);
}