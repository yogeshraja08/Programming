import java.util.Scanner;

public class Day6 {
    public static void main(String[] args) {
        // print last half as reverse
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number/word : ");
        String number = input.next();
        String rev = "", num = "";
        for(int j=0; j<number.length()/2; j++){
            num += number.charAt(j);
        }
        for(int i = number.length()-1; i>=number.length()/2; i--){
            rev += number.charAt(i);
        }
        //System.out.println(num+rev);
        try{
            int k=Integer.parseInt(num+rev);
            System.out.println(k);
        }
        catch(Exception e){
            // System.out.println(e);
            System.out.println(num+rev);
        }
        input.close();
    }
}
