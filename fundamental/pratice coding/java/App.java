import java.util.Scanner;
public class App {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        double sum = 0;
        int count = 0;
        double maxn=-999999,minn=999999;
        while(true){
            System.out.println("enter number");
            double num = kb.nextDouble();
            if(num >=0) {
                sum+=num; 
                count++;
                if(num < minn) minn = num;
                if(num > maxn) maxn = num;

            }
            else if(num<0)break;
        }
        System.out.println(sum);
        System.out.println(sum/count);
        System.out.println(minn+"min and max"+maxn);
    }

    
}
