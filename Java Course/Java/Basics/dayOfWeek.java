import java.util.Scanner;
import java.util.Date;
import java.util.Calendar;

public class dayOfWeek {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // System.out.print("Enter the day number : ");
        // int dayOfWeek = input.nextInt();
        
        Date date=new Date();
        Calendar c = Calendar.getInstance();
        c.setTime(date);
        int dayOfWeek = c.get(Calendar.DAY_OF_WEEK);
        System.out.println("Day of week in number is "+dayOfWeek);
        
        switch (dayOfWeek){
            case 1:
                System.out.println("So, Today is Sunday");
                break;
            case 2:
                System.out.println("So, Today is Monday");
                break;
            case 3:
                System.out.println("So, Today is Tuesday");
                break;
            case 4:
                System.out.println("So, Today is Wednesday");
                break;
            case 5:
                System.out.println("So, Today is Thursday");
                break;
            case 6:
                System.out.println("So, Today is Friday");
                break;
            case 7:
                System.out.println("So, Today is Saturday");
                break;
        }

        input.close();
    }
}
