public class Args {
    public static void main(String[] args) {
        summary(5,7,2,8,1);
    }
    public static void summary(int ... num){
        int sum = 0;
        for(int i=0;i<num.length;i++){
            sum +=num[i];
        }
        System.out.println(sum);
    }
}
