import java.util.LinkedHashSet;
import java.util.TreeSet;
public class LinkedHashSet_ {
    public static void main(String[] args) {
        LinkedHashSet<Double> a = new LinkedHashSet<>();
        TreeSet<Double> b = new TreeSet<>();
        a.add(10.0);
        b.add(10.0);
        b.add(1.0);
        a.add(1.0);
        for (Double double1 : b) {
            System.out.println(double1);
            
        }
        for (Double i : a) {
            System.out.println(i);
            
        }
    }
    
}
