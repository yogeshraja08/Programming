import java.util.Scanner;
public class Basics {
    public static void main(String[] args) {
        System.out.println("hello world");

        System.out.print("Enter the number to show multiplication table : ");
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        for (int i=0; i<=20; i++){
            System.out.println(i+" * "+num+" = "+i*num);
        }

        System.out.print("Enter your name : ");
        String name = input.next();
        System.out.println("YoN and "+name+" are friends....");
        input.close();
    }
}

// left shift "<<"
// 10<<2
// 10 - 1010
// 1st shift - 10100
// 2nd shift - 101000
// 101000 - 40

// right shift ">>"
// 10>>2
// 10 - 1010
// 1st shift - 101
// 2nd shift - 10
// 10 - 2