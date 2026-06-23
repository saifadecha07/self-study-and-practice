import java.io.*;
public class IOlearn {
    public static void main(String[] args) {
        File f = new File("C:\\Users\\saifa\\Desktop\\agoda\\fundamental\\pratice coding\\java\\test.txt");
        try {
            FileWriter writer = new FileWriter(new File("agoda.text"));
            BufferedWriter bw = new BufferedWriter(writer);
            bw.write("Agoda is calling me man ");
            bw.write("Agoda please I really like that place");
            writer.write("Hello world ");
            writer.write("I love my jobs \n");
            bw.close();// close เพื่อให้ได้ข้อความด้วย ปิดทีเดียวพอ
            // writer.close(); 
            System.out.println("already write");
        } catch (java.lang.Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
}
