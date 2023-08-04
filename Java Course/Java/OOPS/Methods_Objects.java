// public class Methods_Objects {
//         public static int sum(){
//                 int b=10;
//                 int c=20;
//                 int a=b+c;
//                 return a;
//         }
//         public static void main(String[] args){
//                 System.out.println(sum());
//         }
// }

// class Anime{
//         String name1 = "one piece";
//         String name2 = "naruto";
//         void display(){
//                 System.out.println(name1+" "+name2);
//         }
// }
// public class Methods_Objects {
//         public static void main(String[] args) {
//                 Anime ani = new Anime();
//                 // System.out.println(ani.name1);
//                 ani.display();
//         }
// }

// public class Methods_Objects {
//         void Basic(){
//                 System.out.println("printing basic method");
//         }
//         void Demo(String name1, String name2){
//                 System.out.println(name1+" "+name2);
//         }
//         public static void main(String[] args) {
//                 Methods_Objects myObj = new Methods_Objects();
//                 myObj.Demo("yon", "sid");
//                 myObj.Basic();
//         }
// }

// // method overloading
// public class Methods_Objects {
//         void sum(int a, int b){
//                 int d = a+b;
//                 System.out.println(d);
//         }
//         void sum(int a){
//                 int c = a+10;
//                 System.out.println(c);
//         }
//         void sum(String a){
//                 System.out.println(a);
//         }
//         public static void main(String[] args) {
//                 Methods_Objects myObj = new Methods_Objects();
//                 myObj.sum(10);
//                 myObj.sum(20, 30);
//                 myObj.sum("Overloading by changing datatypes");
//         }
// }

// // method overriding
// class demo{
//         void method(){
//                 System.out.println("demo");
//         }
// }
// public class Methods_Objects extends demo{
//         void method(){
//                 System.out.println("methods objects");
//         }
//         public static void main(String[] args) {
//                 Methods_Objects myObj = new Methods_Objects();
//                 myObj.method();
//         }
// }