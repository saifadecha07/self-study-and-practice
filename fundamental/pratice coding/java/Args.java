public class Args {
    public static void main(String[] args) {
        summary(5,7,2,8,1);
        connect(101);
    }
    public static void summary(int ... num){
        int sum = 0;
        for(int i=0;i<num.length;i++){
            sum +=num[i];
        }
        System.out.println(sum);
    }
    public static void connect(int ping){
        if(ping > 100) return;
        System.out.println("ping = "+ping);
    }
}
