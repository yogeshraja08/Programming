#include<stdio.h>
void main(){
    int row,col;
    printf("Enter the no. of rows : ");
    scanf("%d",&row);
    printf("Enter the no. of cols : ");
    scanf("%d",&col);
    printf("Getting the values of the matrix......\n");
    int arr[row][col];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("Enter the %d x %d value : ",i,j);
            scanf("%d",&arr[i][j]);
        }
    }
    int sum=0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (i==j)
            {
                sum += arr[i][j];
            }
        }
    }
    printf("Sum of the left diagonal of the matrix is %d",sum);
}