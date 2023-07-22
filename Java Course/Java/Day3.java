import java.util.*;
public class Day3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // System.out.print("Enter the number 1 : ");
        // int num1 = input.nextInt();
        // System.out.print("Enter the number 2 : ");
        // int num2 = input.nextInt();
        // System.out.print("Enter the number 3 : ");
        // int num3 = input.nextInt();

        // if ((num1>num2) && (num1>num3)){
        //     System.out.println("Number 1 is biggest number");
        // }
        // else if ((num1<num2) && (num1<num3)){
        //     System.out.println("Number 1 is smallest number");
        // }
        // else if ((num1 == num2) || (num2 == num3)){
        //     System.out.println("Two of the given numbers are same");
        // }
        // else{
        //     System.out.println("number 1 is "+num1);
        //     System.out.println("number 2 is "+num2);
        //     System.out.println("number 3 is "+num3);
        // }



    //     int a = input.nextInt();
    // //datatype var = (condition) ? true:false;
    //     String max = ((((a%2==0) || (a==10)) && a>0) ? "even":"odd" );
    //     System.out.println(max);


    
    // System.out.print("Enter the day number : ");
    // int week = input.nextInt();
    
    // Date date=new Date();
    // Calendar c = Calendar.getInstance();
    // c.setTime(date);
    // int dayOfWeek = c.get(Calendar.DAY_OF_WEEK);
    // System.out.println("Day of week in number is "+dayOfWeek);
    
    // switch (dayOfWeek){
    //     case 1:
    //         System.out.println("So, Today is Monday");
    //         break;
    //     case 2:
    //         System.out.println("So, Today is Tuesday");
    //         break;
    //     case 3:
    //         System.out.println("So, Today is Wednesday");
    //         break;
    //     case 4:
    //         System.out.println("So, Today is Thursday");
    //         break;
    //     case 5:
    //         System.out.println("So, Today is Friday");
    //         break;
    //     case 6:
    //         System.out.println("So, Today is Saturday");
    //         break;
    //     case 7:
    //         System.out.println("So, Today is Sunday");
    //         break;
    // }



        // System.out.print("Enter start number : ");
        // int a = input.nextInt();
        // System.out.print("Enter end number : ");
        // int b = input.nextInt();
        // int sum=0, evenSum=0, oddSum=0;
        // for(int i = a;i<=b;i++){
        //     if(i%2==0){
        //         evenSum+=i;
        //     }
        //     else{
        //         oddSum+=i;
        //     }
        //     sum+=i;
        // }
        // System.out.println("Sum of the total numbers is "+sum);
        // System.out.println("Sum of the even numbers is "+evenSum);
        // System.out.println("Sum of the odd numbers is "+oddSum);


            // condition for prime numbers -- method 1
        // System.out.print("Enter the number : ");
        // int num = input.nextInt();
        // boolean check = false;
        // for (int i=2; i<=num/2;i++){
        //     if(num % i == 0){
        //         check = true;
        //         break;
        //     }
        // }
        // if (check == false){
        //     System.out.println("It is prime");
        // }
        // else{
        //     System.out.println("It is not a prime");
        // }

        
        //     // condition for prime -- method 2
        // System.out.print("Enter the number : ");
        // int number = input.nextInt();
        // int factor = 0;
        // for (int i=2; i<=number; i++){
        //     if(number%i == 0){
        //         factor++;
        //     }
        // }
        // if(factor==1){
        //     System.out.println("It is prime");
        // }
        // else{
        //     System.out.println("It is not prime");

        // }

            // condition for sum of prime numbers
        System.out.print("Enter the starting number : ");
        int a = input.nextInt();
        System.out.print("Enter the ending number : ");
        int b = input.nextInt();
        int primesum = 0;
        for(int j=a; j<=b; j++)
        {   
            int num = j;
            int factor = 0;
            for (int i=2; i<=num;i++){
                if(num%i==0){
                    factor++;
                }
            }
            if (factor==1){
                primesum+=j;
            }
        }
        System.out.println(primesum);
        //     // condition for prime numbers -- method 2
        // System.out.print("Enter the starting number : ");
        // int a = input.nextInt();
        // System.out.print("Enter the ending number : ");
        // int b = input.nextInt();
        // int primesum = 0;
        // for(int j=a; j<=b; j++)
        // {   
        //     int num = j;
        //     int factor = 0;
        //     for (int i=2; i<=num;i++){
        //         if(num%i==0){
        //             factor++;
        //         }
        //     }
        //     if (factor==1){
        //         primesum+=j;
        //     }
        // }
        // System.out.println(primesum);
        


        //     // fibnosi serious
        // System.out.print("Enter the range : ");
        // int num = input.nextInt();
        // int n1=0,n2=1;
        // System.out.print(n1 + " " + n2 + " ");
        // for (int i=1; i<=num;i++){
        //     int n3 = n1 + n2;
        //     System.out.print(n3+" ");
        //     n1 = n2;
        //     n2 = n3;
        // }






        input.close();
    }
}
