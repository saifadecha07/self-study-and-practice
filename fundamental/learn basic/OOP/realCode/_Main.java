
public class _Main {
    public static void main(String[] args) {
        Employee emp1 = new Employee("Saifa Decha",25000.0);
        System.out.println(emp1.getInfo());
        System.out.println(emp1.getName()+" "+emp1.getSalary());
        Employee.showNum();
        Company.job();
    }
}
