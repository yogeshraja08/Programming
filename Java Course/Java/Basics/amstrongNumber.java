import java.util.Scanner;

public class amstrongNumber {
    public static void main(String[] args) {
        //  amstrong number
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number : ");
        int num = input.nextInt();
        int temp = num, digits=0, last=0, sum=0;
        while(temp>0){
            temp = temp/10;   
            digits++;   
        }   
        temp = num;   
        while(temp>0){    
            last = temp % 10;   
            sum += (Math.pow(last, digits));
            temp = temp/10;
        }
        if (num == sum){
            System.out.println("amstrong");
        }
        else{
            System.out.println("not amstrong");
        }
        input.close();
    }
}
