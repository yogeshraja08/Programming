import java.util.*;
public class Day1{
    public static void main(String[] args) {
        System.out.println("hello world");
        int a=1;
        while (a==1){
            System.out.print("Enter the number : ");
            Scanner number = new Scanner(System.in);
            int no = number.nextInt();
            for (int i=0; i<=20; i++){
                System.out.println(i+"*"+no+"="+i*no);
            }
            System.out.println("If you want to continue, Press '1' or else Press '0' \t");
            int check = number.nextInt();
            if (check == 1){
                System.out.println("Programming is going to running again......");
            }
            else{
                break;
            }
        number.close();
        }

        Scanner input = new Scanner(System.in);
        System.out.print("Enter name 1 : ");
        String name1 = input.nextLine();
        System.out.print("Enter name 2 : ");
        String name2 = input.nextLine();
        System.out.println(name1+" and "+name2+" are friends....");
        input.close();
    }
}