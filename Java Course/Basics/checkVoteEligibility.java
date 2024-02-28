import java.util.Scanner;

public class checkVoteEligibility {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);

        System.out.print("Enter your name : ");
        String name = myObj.next();
        
        System.out.print("Enter your Password : ");
        String pwd = myObj.next();
        
        System.out.print("Enter your age : ");
        int age = myObj.nextInt();
        
        if (age>18){
            if (name==pwd){
                System.out.println("HI "+name+" WELCOME!!");
                System.out.println("You are eligible for vote!!!");
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
