import java.util.Scanner;

public class Day5 {
    public static void main(String[] args) {
        //  //  substring
        // String a = "yogesh raja";
        // System.out.println(a.indexOf('y'));
        // System.out.print(a.substring(0,1).toUpperCase());
        // System.out.print(a.substring(1,6).toLowerCase());
        // System.out.print(a.substring(6,7));
        // System.out.print(a.substring(7,8).toUpperCase());
        // System.out.print(a.substring(8).toLowerCase());


        //  // StringBuffer - can append values
        //  // String - cannot append values
        // StringBuffer txt = new StringBuffer("yon");
        // String a = "yogesh";
        // System.out.println(txt.capacity());
        // System.out.println(txt.append(" raja"));
        // // System.out.println(a.append(" raja"));
        // System.out.println(txt.replace(2 , 3, "gesh"));
        // System.out.println(txt.delete(0, 2));
        // System.out.println(txt.insert(2, " "));


        // int a=10;
        // float b=20.22255f;
        // String c = String.valueOf(a);
        // String d = String.valueOf(b);
        // System.out.println(c+d);


        // String a = "hi guru".trim();
        // Boolean b = a.startsWith("hi");
        // System.out.println(b);


        // String name = "yogesh";
        // for (int i = 0; i<name.length();i++){
        //     char c = name.charAt(i);
        //     System.out.println(c);
        // }
        
        // palindrome
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the word : "); //madam
        String name = input.next();
        String rev = "";
        for(int i = name.length()-1;i>=0;i--){
            rev+=name.charAt(i); //rev = rev + name.charAt(i); 
        }

        if(name.equals(rev)){
            System.out.println("It is palindrome");
        }
        else{
            System.out.println("It is not palindrome");
        }

        input.close();

        //  //  no. of vowels in given word
        // Scanner input = new Scanner(System.in);
        // System.out.print("Enter the word : ");
        // String name1 = input.next();
        // String name = name1.toLowerCase();
        // int count = 0;
        // for(int i=0; i<name.length();i++){
        //     if (name.charAt(i) == 'a' || name.charAt(i) == 'e' || name.charAt(i) == 'i' || name.charAt(i) == 'o' || name.charAt(i) == 'u'){
        //         count++;
        //     }
        // }
        // System.out.println(count);
        // input.close();


        //  //  amstrong number
        // Scanner input = new Scanner(System.in);
        // System.out.print("Enter the number : ");
        // int num = input.nextInt();
        // int temp = num, digits=0, last=0, sum=0;
        // while(temp>0){
        //     temp = temp/10;   
        //     digits++;   
        // }   
        // temp = num;   
        // while(temp>0){    
        //     last = temp % 10;   
        //     sum += (Math.pow(last, digits));
        //     temp = temp/10;
        // }
        // if (num == sum){
        //     System.out.println("amstrong");
        // }
        // else{
        //     System.out.println("not amstrong");
        // }
        // input.close();


        //  //  anagram
        // Scanner input = new Scanner(System.in);
        // System.out.print("Enter the word 1 : ");
        // String word1 = input.nextLine();
        // System.out.print("Enter the word 2 : ");
        // String word2 = input.nextLine();
        // int count = 0;
        // if(word1.length() == word2.length()){
        //     for(int i=0; i<word1.length(); i++){
        //         for(int j=0; j<word2.length(); j++){
        //             if(word1.charAt(i) == word2.charAt(j)){
        //                 count++;
        //                 break;
        //             }
        //         }
        //     }
        // }
        // if(count == word1.length()){
        //     System.out.println("Anagram");
        // }
        // else{
        //     System.out.println("not Anagram");
        // }
        
        // input.close();
    }
}