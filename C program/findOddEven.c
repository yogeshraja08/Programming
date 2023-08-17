#include <stdio.h>

void main(){
    printf("Enter the number : ");
    int num,countEven=0,countOdd=0,digit;
    scanf("%d",&num);
    while (num>0)
    {
        digit = num % 10;
        if (num%2==0){
            countEven++;
        }
        else{
            countOdd++;
        }
        num = num/10;
    }
    printf("The count of even digits is %d, The count of Odd digits is %d",countEven,countOdd);
}