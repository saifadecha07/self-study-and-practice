import java.util.Scanner;

public class BMI {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter your weight = ");
        double weight = sc.nextDouble();
        System.out.print("ehhh");
        System.out.print("yeee");
        System.out.print("enter your height in cm = ");
        double height = sc.nextDouble();
        height /= 100;
        double bmi = weight / (height * height);
        System.out.println(bmi);
        // assign 3
        if (bmi < 18 & bmi > 0) {
            System.out.println("lower than standard");
        } else if (18.5 <= bmi & bmi <= 22.9) {
            System.out.println("It's ok");
        } else if (23.0 <= bmi & bmi <= 29.9) {
            System.out.println("It might be a little chubby");
        } else if (bmi >= 30) {
            System.out.println("higher than standard");
        } else {
            System.out.println("invalid BMI");
        }

        // switch ใช้ double ตรงๆ ไม่ได้ ต้อง cast เป็น int ก่อน
        int bmiInt = (int) bmi;
        switch (bmiInt) {
            case 20:
            case 21:
            case 22:
                System.out.println("normal range");
                break;
            default:
                System.out.println("out of normal range");
                break;
            // default เป็น case สุดท้ายเสมอ → ไม่มี code
            // ต่อให้ fall-through ไป → break ไม่มีผล แต่ใส่ไว้เพื่อ
            // consistency และป้องกันลืมถ้าเพิ่ม case ทีหลัง
        }

    }
}
