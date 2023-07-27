// interface - all methods are abstract by default
// interface is not a class
interface Robot{
    void sensor();
    // to declare non abstract method use "default"
    default void sense(){
        System.out.println("Non abstract method in interface");
    }

}
public class Interface implements Robot{
    public void sensor(){
        System.out.println("hii");
    }
    public static void main(String[] args) {
        Interface myObj = new Interface();
        myObj.sensor();
        myObj.sense();
    }
}
