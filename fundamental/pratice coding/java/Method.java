public class Method {
    public static void main(String[] args) {
        display();
        plus(5,7);
        int[] a = {5,7,8,9,2,100};
        System.out.println(displaySize());
        double size = calculateSize(10, 7);
        System.out.println(size);
        System.out.println(maxNum(8, 70));
        System.out.println(maxaar(a));
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
    private static double calculateSize(double x,double y){
        double size = x*y*y/10;
        return size;
    }
    public static int maxNum(int x,int y){
        if(x>y) return x;
        else return y;

    }
    public static int maxaar(int[] a){
        int max = a[0];
        for(int i=0;i<a.length;i++){
            if(a[i]>max) max = a[i];
        }
        return max;
    }
}
