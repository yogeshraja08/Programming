import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class test {
    public static List <Object> functional(){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number 1 : ");
        int num1 = input.nextInt();
        System.out.print("Enter the number 2 : ");
        int num2 = input.nextInt();
        int sum,sub,mul,div,rem;
        sum = num1+num2;
        sub = num1-num2;
        mul = num1*num2;
        div = num1/num2;
        rem = num1%num2;
        input.close();
        return Arrays.asList(sum,sub,mul,div,rem);
    }
    void display(){
        List <Object> operators = functional();
        System.out.println(operators);
    }
    public static void main(String[] args) {
        test myObj = new test();
        myObj.display();
    }
}