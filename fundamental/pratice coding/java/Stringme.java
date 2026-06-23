public class Stringme {
    public static void main(String[] args) {
        String name = new String("SKy");
        String name1 = "skY";
        String city = "bangkok";
        System.out.println(name+city+name.length());
        System.out.println(name.charAt(2));
        System.out.println(name1.equalsIgnoreCase(name));
        System.out.println(name.startsWith("S"));//endWith and it can be "str long char"
        System.out.println(city.indexOf("k"));
        String massage = "hello 2026 2026 2026";
        String message = massage.replaceFirst("2026","2000");
        System.out.println(message);
        System.out.println(massage);
        String data ="mango,orange,durian,juice,dragon";
        String[] fruit = data.split(",");
        System.out.println(fruit[2]);
        for(String i:fruit){
            if(i!=fruit[0]  & i != fruit[fruit.length-1]){
                System.out.print(" "+i);
            }    
            else if(i.equals(fruit[fruit.length-1])){
                System.out.println(" "+i);
            }
            else System.out.print(i);
        }
        String nameCity = city.substring(0,4);
        System.out.println(nameCity);
        char[] nameword = name.toCharArray();
        for(Character i:nameword){
            System.out.print(i+" ");
        }
        char[] name_s = {'s','k','y'};
        System.out.println(String.copyValueOf(name_s));

        String city1 = "ranong   ";
        System.out.println(city1.trim().toUpperCase()); 
        double num = 200;
        System.out.println(String.valueOf(num).toUpperCase());
    }
}
