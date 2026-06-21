import java.util.Scanner;
public class assign1 {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        // program compare 2 number
        System.out.print("enter number 1 ");
        double num1 = kb.nextDouble();
        System.out.print("enter number 2 ");
        double num2 = kb.nextDouble();
        kb.close();
        if (num1>num2){
            System.out.println("num1 > num 2");
        }
        else if(num2>num1){
            System.out.println("num 2 > num 1");
        }
        else{
            System.out.println("num1 "+ num1+"="+" num2 = "+num2);
        }
    }
}
