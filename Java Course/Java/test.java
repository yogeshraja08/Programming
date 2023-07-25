import java.util.*;
public class test {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the range : ");
        int range = input.nextInt();
        // int range = 10;
        String str = "*";
        String temp = " ";
        for(int i=0; i<=range; i++){
            System.out.println(str);
            str = temp + str;
        }
        // input.close();
    }
}