import java.util.InputMismatchException;
import java.util.Scanner;
public class ExceptionPractice {
    public static void main(String[] args) {
        double balance =100;
        try (Scanner kb = new Scanner(System.in)) {
            System.out.println("enter your with draw");
            int cash = kb.nextInt();
            if(cash<0){throw new java.lang.Exception("pls positive num");}
            balance = (100/cash);
            System.out.println(balance);
            String [] bank = {"A0","B1"};
            System.out.println(bank[1]);


        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
            // ผิดพลาดมาส่วนนี้
        } catch (IndexOutOfBoundsException e){
            System.out.println("out range man");
        } catch(InputMismatchException e){
            System.out.println("only number");
        } catch (java.lang.Exception e){
            System.out.println("unexpected: " + e.getMessage());
        }finally{
            System.out.println("shutdown server");
            System.out.println("locked DB");
        }
    }
    public static void withdraw(int amount) throws java.lang.Exception {
        if(amount<0){
            throw new java.lang.Exception("no negative number");
        }
        System.out.println(amount);
    }
}
