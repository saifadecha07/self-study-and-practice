import java.util.InputMismatchException;
import java.util.Scanner;
public class Exception {
    public static void main(String[] args) {
        double balance =100;
        try (Scanner kb = new Scanner(System.in)) {
            System.out.println("enter your with draw");
            int cash = kb.nextInt();
            balance = (100/cash);
            System.out.println(balance);
            String [] bank = {"A0","B1"};
            System.out.println(bank[50]);

            
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
            // ผิดพลาดมาส่วนนี้
        } catch (IndexOutOfBoundsException e){
            System.out.println("out range man");
        } catch(InputMismatchException e){
            System.out.println("only number");
        }finally{
            System.out.println("shutdown server");
            System.out.println("locked DB");
        }
    }
}
