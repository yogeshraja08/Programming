import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        // palindrome
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the word : "); //madam
        String name = input.next();
        String rev = "";
        for(int i = name.length()-1;i>=0;i--){
            rev+=name.charAt(i);
        }
        
        if(name.equals(rev)){
            System.out.println("It is palindrome");
        }
        else{
            System.out.println("It is not palindrome");
        }

        input.close();
    }
}
