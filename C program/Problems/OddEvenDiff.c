#include<stdio.h>

int countOddEvenDifference(int size, int arr[]){
    int evenCount=0, oddCount=0, OddEvenDiff;
    for (int i=0; i<size;i++){
        if (arr[i]%2==0)
        {
            evenCount+=1;
        }
        else
        {
            oddCount+=1;
        }
    }
    OddEvenDiff = oddCount - evenCount;
    return OddEvenDiff;
}

int main(){
    int size;
    scanf("%d",&size);
    int arr[size];
    for (int i=0; i<size; i++){
        scanf("%d",&arr[i]);
    }
    int diff = countOddEvenDifference(size,arr);
    printf("%d",diff);
    return 0;
}