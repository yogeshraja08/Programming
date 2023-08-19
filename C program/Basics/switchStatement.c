#include <stdio.h>
void main(){
    int choise;
    printf("Enter the choise : ");
    scanf("%d",&choise);
    switch (choise)
    {
        case 1:
            printf("You have selected case 1");
            break;
        case 2:
            printf("You have selected case 2");
            break;
        case 3:
            printf("You have selected case 3");
            break;
        case 4:
            printf("You have selected case 4");
            break;
        default:
            printf("You entered a wrong option");
            break;
    }
}