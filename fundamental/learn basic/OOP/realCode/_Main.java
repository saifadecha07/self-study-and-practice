
public class _Main {
    public static void main(String[] args) {
        Company.job();
        Programmer saifa = new Programmer("Sky");
        saifa.setName("Saifa");
        saifa.setID("7");
        saifa.getInfo();
        System.out.println(saifa);
        Sexworker seife = new Sexworker("ski");
        System.out.println(seife);
        Programmer si = new Programmer("si");
        System.out.println(si.showskill());
        //Employee si = new Programmer("si"); ใช้ method class programmer ไม่ได้
        Man a = new Man();
        a.setName("OOP");
        System.out.println(a);
        System.out.println(saifa.getSalary());
        System.out.println(saifa.showskill("java","python","OOP"));
        saifa.bonus();
    }
}
