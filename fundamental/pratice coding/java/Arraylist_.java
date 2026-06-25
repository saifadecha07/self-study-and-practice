
import java.util.*;
public class Arraylist_ {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<String> b = new ArrayList<>(List.of("sky","mittra","gf","Agoda"));
        a.add(10);
        a.add(0,55);
        for (Integer i : a) {
            System.out.println(i);
            
        }
        a.set(0, 5);
        System.out.println(a.size()+" "+a.get(0));
    }
}
