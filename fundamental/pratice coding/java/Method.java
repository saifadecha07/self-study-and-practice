public class Method {
    public static void main(String[] args) {
        display();
        plus(5,7);
        System.out.println(displaySize());
    }
    public static void display(){
        System.out.println("Hello");
    }
    static void plus(int x,int y){
        System.out.println("x + y = "+(x+y));
    }
    private static int displaySize(){
        return 54;
    }
}
