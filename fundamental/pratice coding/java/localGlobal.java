public class localGlobal {
    public static void main(String[] args) {
        int b = 10; // global variable work on main
        System.out.println(b);
        {
            int c = 10; //local variable
            System.out.println(b+c);
        }
        if(b==10){ 
            final int A = 50; // local variable
            System.out.println(b+A);
        }
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Character.MAX_VALUE);
    }
}
