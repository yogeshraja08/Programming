abstract class moment{
    moment(){
        System.out.println("Eating food");
    }
    abstract void walk();
    void sleep(){
        System.out.println("Sleeping in bed");
    }
}
public class AbstractClass extends moment{
    void walk(){
        System.out.println("Walk by leg");
    }
    public static void main(String[] args) {
        moment mnt;
        mnt = new AbstractClass();
        mnt.sleep();
        mnt.walk();
    }
}
