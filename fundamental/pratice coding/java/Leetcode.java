import java.io.*;
import java.util.Scanner;

public class Leetcode {
    //pratice solving problem with java from my tutor part 1
    public static void main(String[] args) {
        try {
            File f = new File("score.text");
            //scanner ก็อ่าน path 
            Scanner input = new Scanner(new File("score.text"));
            String student = "";
            while(input.hasNext()){
                student = input.nextLine();
                int pos = student.indexOf(" ");
                String score = student.substring(pos,student.length());
                score = score.trim();
                double sc = Double.parseDouble(score);
                if(sc>=80 && sc<=100 ){System.out.printf("%s get grade A %n",student);}
                else if(sc>=70){System.out.println(student+" grade B");}
                else if(sc<70 && sc>=0){System.out.println(student+" grade F");}
                else throw new java.lang.Exception("InvalidInput");

            }
        } catch (java.lang.Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
        
        
    }
}
