public class stringFuntions {
    public static void main(String[] args) {
        //  substring
        String a = "yogesh raja";
        System.out.println(a.indexOf('y'));
        System.out.print(a.substring(0,1).toUpperCase());
        System.out.print(a.substring(1,6).toLowerCase());
        System.out.print(a.substring(6,7));
        System.out.print(a.substring(7,8).toUpperCase());
        System.out.print(a.substring(8).toLowerCase());


        // StringBuffer - can append values
        // String - cannot append values
        StringBuffer txt = new StringBuffer("yon");
        System.out.println(txt.capacity());
        System.out.println(txt.append(" raja"));
        // System.out.println(a.append(" raja"));
        System.out.println(txt.replace(2 , 3, "gesh"));
        System.out.println(txt.delete(0, 2));
        System.out.println(txt.insert(2, " "));


        int a1=10;
        float b=20.22255f;
        String c = String.valueOf(a1);
        String d = String.valueOf(b);
        System.out.println(c+d);


        String a2 = "hi guru".trim();
        Boolean b2 = a2.startsWith("hi");
        System.out.println(b2);


        String name = "yogesh";
        for (int i = 0; i<name.length();i++){
            char c2 = name.charAt(i);
            System.out.println(c2);
        }
        
    }
}
