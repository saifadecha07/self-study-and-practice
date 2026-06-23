import java.io.*;
public class IOread {
    public static void main(String[] args) {
        try {
            FileReader f = new FileReader(new File("agoda.text"));
            // int data ;
            // while((data = f.read())!=-1){
            //     System.out.println(data);
            //     System.out.printf("%c\n",data);
            // }
            BufferedReader br = new BufferedReader(f);
            String message ="";
            // อ่านทีละบรรทัดมาเก็บใน message ทำ2ครั้ง มี 2 บรรทัด
            while((message = br.readLine())!=null){
                System.out.println(message);
            }


        } catch (java.lang.Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            System.out.println("File not found? I dont know man");
        }
    }
}
