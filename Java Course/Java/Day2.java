import java.util.*;
public class Day2 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);

        System.out.print("Enter your name : ");
        String name = myObj.nextLine();
        
        System.out.print("Enter your Password : ");
        String pwd = myObj.nextLine();
        
        System.out.print("Enter your age : ");
        int age = myObj.nextInt();
        
        if (age>18){
            if (name==pwd){
                System.out.println("HI SIRANJEEVI, WELCOME");
            }
            else{
                System.out.print("Congratulations, ");
                System.out.println("You are eligible for vote!!!");
            }
        }
        else if(age==18){
            System.out.println("Welcome, You are eligible for vote and you are new to vote");
        }
        else{
            System.out.print("Sorry, ");
            System.out.println("You are not eligible for vote");
        }
    myObj.close();
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