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
    int leftDiaSum=0,rightDiaSum=0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (i==j)
            {
                leftDiaSum += arr[i][j];
            }
        }
    }
    for (int i = 0; i < row; i++)
    {
        size = size-1;
        for (int j = 0; j < col; j++)
        {            
            if (size==j)
            {
                rightDiaSum += arr[i][j];
            }
        }
    }
    printf("Sum of the left diagonal of the matrix is %d\n",leftDiaSum);
    printf("Sum of the right diagonal of the matrix is %d",rightDiaSum);
}

// 0,0     0,1     0,2     0,3
// 1,0     1,1     1,2     1,3
// 2,0     2,1     2,2     2,3
// 3,0     3,1     3,2     3,3