
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