import java.util.Scanner;

public class countVowels {
    public static void main(String[] args) {
        //  no. of vowels in given word
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the word : ");
        String name1 = input.next();
        String name = name1.toLowerCase();
        int count = 0;
        for(int i=0; i<name.length();i++){
            if (name.charAt(i) == 'a' || name.charAt(i) == 'e' || name.charAt(i) == 'i' || name.charAt(i) == 'o' || name.charAt(i) == 'u'){
                count++;
            }
        }
        System.out.println(count);
        input.close();
    }
}
