import javax.sound.sampled.SourceDataLine;

public class Array {
    public static void main(String[] args) {
        int[] a = new int[5];
        int[] b = { 4, 5, 6, 4, 1 };
        System.out.println(a.length + " " + b.length);
        for (int i = 0; i < b.length; i++) {
            System.out.print(b[i] + " ");
        }
        System.out.println(" ");
        for (int num : b) {
            System.out.println(num);
        }
        String[][] fruit = { { "Durian", "Orange" }, { "Orange juice", "Mango juice" } };
        System.out.println(fruit[1][0]);
        for (int feat = 0; feat < fruit.length; feat++) {
            for (int item = 0; item < fruit[item].length; item++) {
                System.out.println(fruit[feat][item]);
            }
        }
    }

}
