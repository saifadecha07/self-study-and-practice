import java.util.HashSet;
public class Hashset_ {
    public static void main(String[] args) {
        HashSet<String> lang = new HashSet<>();
        lang.add("java");
        lang.add("java");
        lang.add("PHP");
        lang.add("SQL");
        lang.remove("PHP");
        for(String i:lang){
            System.out.println(i);
        }
        System.out.println(lang.size());
    }
}
