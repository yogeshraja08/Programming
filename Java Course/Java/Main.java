class A
{
      public static void main(String[] args) {
        
    }
}
class B extends A{
    public void  method() {
        System.out.println("method of class B");
        }
}
class C extends A{
    public void method(){
        System.out.println("method of class C");
    }
}
    class D extends A{
    public void method(){
        System.out.println("method of class D");
    }
}
class Main{
public static void main(String[] args) {
    B o1=new B();
    C o2=new C();
    D o3=new D();

    o1.method();
    o2.method();
    o3.method();

}}

