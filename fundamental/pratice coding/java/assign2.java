import java.util.Scanner;

public class assign2 {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        System.out.print("enter number");
        int num = kb.nextInt();
        String result = (num % 2 == 0) ? "even" : "odd";
        System.out.println(result);
    }
}
