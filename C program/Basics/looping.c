#include<stdio.h>
// do whle
void main(){
    int i=0;
    do{
        printf("*");
        i++;
    } while (i<=10);

    // infinite for loop
    for(;;){    // no initialization, no condition,no end range
        printf("*");
    }
}