// overriding the method overriding
// super - used to call parent class\method
class demo{
        String name = "YoN";
        void method(){
                System.out.println("demo");
        }
        demo(){
                System.out.println("Constructor - parent class");
        }
}
public class Overriding extends demo{
        String name = "Yogesh";
        void method(){
                super.method();
                System.out.println("methods objects");
        }
        void display(){
                System.out.println(super.name);
                System.out.println(name);
        }
        Overriding(){
                super(); // default , not necessary
                System.out.println("Constructor - child class");
        }
        public static void main(String[] args) {
                Overriding myObj = new Overriding();
                myObj.method();
                myObj.display();
        }
}