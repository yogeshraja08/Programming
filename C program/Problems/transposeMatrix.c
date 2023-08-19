#include<stdio.h>
void main(){
    int row,col;
    printf("Enter the no. of rows : ");
    scanf("%d",&row);
    printf("Enter the no. of cols : ");
    scanf("%d",&col);
    printf("Getting the values of the matrix......\n");
    int arr[row][col];
    int size = col;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("Enter the %d x %d value : ",i,j);
            scanf("%d",&arr[i][j]);
        }
    }
    printf("\nPrinting Original Matrix......\n");
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row; j++)
        {
            printf("%d  ",arr[i][j]);
        }
        printf("\n");
    }
    int newArr[col][row];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            newArr[j][i] = arr[i][j];
        }
    }
    printf("\nPrinting Transposed Matrix......\n");
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row; j++)
        {
            printf("%d  ",newArr[i][j]);
        }
        printf("\n");
    }
}