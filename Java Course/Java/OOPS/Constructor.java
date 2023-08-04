// constructor is the mirror of the class
// constructor overloading -  more than 1 constructor in a single class
//  |-> datatype have to be changed or else extra no. of parameters have to be given
public class Constructor {
    String food;
    int count;
    Constructor(String food, int count){
        this.food = food;
        this.count = count;
    }
    void Basic(String food,int count){
        System.out.println(food+" "+count);
    }

    public static void main(String[] args) {
        Constructor myObj = new Constructor("dosa",2);
        myObj.Basic("DOSAI",3);
    }
}