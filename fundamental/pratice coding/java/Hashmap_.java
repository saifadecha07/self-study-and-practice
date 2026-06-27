import java.util.HashMap;
public class Hashmap_ {
    public static void main(String[] args) {
        HashMap<County,String> infoUser = new HashMap<>();
        infoUser.put(County.TH, "Saifa Decha");
        System.out.println(infoUser.get(County.TH));
        System.out.println(infoUser.containsKey(County.JP));
    }
}
enum County {
    TH,JP,CN;
  
}