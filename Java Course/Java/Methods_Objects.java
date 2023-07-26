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

/**
 * Methods_Objects
 */
public class Methods_Objects {
        void Basic(){
                System.out.println("printing basic method");
        }
        void Demo(String name1, String name2){
                System.out.println(name1+" "+name2);
        }
        public static void main(String[] args) {
                Methods_Objects myObj = new Methods_Objects();
                myObj.Demo("yon", "sid");
                myObj.Basic();
        }
}