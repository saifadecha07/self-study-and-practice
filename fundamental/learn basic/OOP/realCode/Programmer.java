
public class Programmer extends Employee {
    public Programmer(String name) { // override
        super(name, 50000); // เรียกก่อนคำสั่งอื่น
        System.out.print("I am programmer");
    }

    public String showskill(){ // overload
        return "vibe code";
    }
    public String showskill(String skill){
    return "skill = "+skill;
    }

    public String showskill(String... skill) {
        String a = "";
        for (String i : skill) {
            a =a+ i;
        }
        return "skill = " + a;
    }
    public void bonus(){
        System.out.println("bouns 50");
    }

}