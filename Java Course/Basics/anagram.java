import java.util.Scanner;

public class anagram {
    public static void main(String[] args) {
        //  anagram
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the word 1 : ");
        String word1 = input.nextLine();
        System.out.print("Enter the word 2 : ");
        String word2 = input.nextLine();
        int count = 0;
        if(word1.length() == word2.length()){
            for(int i=0; i<word1.length(); i++){
                for(int j=0; j<word2.length(); j++){
                    if(word1.charAt(i) == word2.charAt(j)){
                        count++;
                        break;
                    }
                }
            }
        }
        if(count == word1.length()){
            System.out.println("Anagram");
        }
        else{
            System.out.println("not Anagram");
        }
        
        input.close();
    }
}
