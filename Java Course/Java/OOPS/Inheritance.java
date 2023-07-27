public class Inheritance extends Parent{
    void ChildDisplay(){
        String vehicle = "car";
        int model = 2023;
        System.out.println(vehicle+" "+model);
    }
    public static void main(String[] args) {
        Inheritance myObj = new Inheritance();
        myObj.ChildDisplay();
        myObj.ParentDisplay();
    }
}
class Parent{
    void ParentDisplay(){
        String vehicle = "bike";
        int model = 2022;
        System.out.println(vehicle+" "+model);
    }
}
