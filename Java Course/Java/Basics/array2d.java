import java.util.Scanner;

public class array2d {
    public static void main(String[] args) {
        // 2D array
        // int arr[][]={{1,2,3},{4,5,6},{7,8,9}};
        Scanner input = new Scanner(System.in);
        System.out.println("Getting values for matrix 1 ....");
        System.out.print("Enter the no. of rows : ");
        int row1 = input.nextInt();
        System.out.print("Enter the no. of columns : ");
        int col1 = input.nextInt();
        int[][] arr1 = new int[row1][col1];
        for (int i=0; i<row1; i++){
            for (int j=0; j<col1; j++){
                System.out.print("Enter the matrix - A"+i+j+" : ");
                arr1[i][j] =  input.nextInt();
            }
        }

        System.out.println("\nGetting values for matrix 2 ....");
        System.out.print("Enter the no. of rows : ");
        int row2 = input.nextInt();
        System.out.print("Enter the no. of columns : ");
        int col2 = input.nextInt();
        int[][] arr2 = new int[row2][col2];
        for (int i=0; i<row2; i++){
            for (int j=0; j<col2; j++){
                System.out.print("Enter the matrix - B"+i+j+" : ");
                arr2[i][j] =  input.nextInt();
            }
        }

        System.out.println("Printing Matrix 1 ..... ");
        for (int i=0; i<row1; i++){
            for (int j=0; j<col1; j++){
                System.out.print(arr1[i][j]+" ");
            }
            System.out.println();
        }
        
        System.out.println("Printing Matrix 2 ..... ");
        for (int i=0; i<row2; i++){
            for (int j=0; j<col2; j++){
                System.out.print(arr2[i][j]+" ");
            }
            System.out.println();
        }

        if(row1==row2 && col1==col2){
            int[][] newArr = new int[row1][col1];
            System.out.println("Addition of matrix 1 and matrix 2 are ");
            for(int i=0; i<row1; i++){
                for (int j=0; j<col1; j++){
                    newArr[i][j] = arr1[i][j] + arr2[i][j];
                    System.out.print(newArr[i][j]+" ");
                }
                System.out.println();
            }
            
            System.out.println("Subtraction of matrix 1 and matrix 2 are ");
            for(int i=0; i<row1; i++){
                for (int j=0; j<col1; j++){
                    newArr[i][j] = arr1[i][j] - arr2[i][j];
                    System.out.print(newArr[i][j]+" ");
                }
                System.out.println();
            }
        }

        if (row1==col2){
            int[][] newarr = new int[col1][row2];
            System.out.println("Multiplication of matrix 1 and matirx 2 are ");
            for(int i=0; i<row1; i++){
                for(int j=0; j<col2; j++){
                    newarr[i][j] = 0;
                    for(int k=0; k<newarr.length; k++){
                        newarr[i][j] += arr1[i][k] * arr2[k][j];
                    }
                    System.out.print(newarr[i][j]+" ");
                }
                System.out.println();
            }
        }

        if (row1==col1) {
            int[][] newTarr = new int[col1][row1];
            System.out.println("Transpose of the matrix 1 is ");
            for (int i=0; i<row1; i++){
                for (int j=0; j<col1; j++){
                    newTarr[i][j] = arr1[j][i];
                    System.out.print(newTarr[i][j]+" ");
                }
                System.out.println();
            }
        }
        input.close();
    }
}
