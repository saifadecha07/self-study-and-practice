

public class Generic_ {
    public static void main(String[] args) {
        System.out.println("oH man do u like Agoda");
        Item<String> Obj1 = new Item<>("Free six 67 to night");
        System.out.println(Obj1.data);
        Float[] l = {1f,3.0f,5.01f};
        String[] s = { "Hi", "sky" };
        Data.showArray2(l);
        Data.showArray(s);
        int a = Data.sh(l);
        System.out.println(a);
    }
}

// package - private
class Item<T extends String> {
    T data;

    public Item(T vaule) {
        data = vaule;
    }
}

class Data<T> {
    static <T> int sh(T[] x){
        int c = 0;
        for (T t : x) {
            System.out.println(t);    
            c++;        
        }
        return c;
      

    }
    static void showArray(String[] str) {  //ถ้าอยากให้ใช้ได้ทุก class
        for (String i : str) {
            System.out.println(i);
        }
    }
    static void showArray2(Object[] obj){
        for(Object i: obj){
            System.out.println(i);
        }
    }
}