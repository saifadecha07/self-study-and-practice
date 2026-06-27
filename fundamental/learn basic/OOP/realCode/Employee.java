public class Employee {
    private static int count=0;
    private String id; //encapsulation a employee may be like this 
    private String name;
    private double salary;
    
    public Employee(String name) { // the way we can create the object
        this.id = String.valueOf(++count);
        this.name = name;
    }
    public Employee(String name,double salary){ //the way we can create the object 
        this.id = String.valueOf(++count);
        this.name = name; this.salary = salary;
    }
    public void setName(String name){ //set name safety
        this.name = name;
    }
    public void setID(String id){
        this.id = id;
    }
    public void setSalary(double salary){
        this.salary = salary;
    }
    public String getInfo(){
        return "ID :"+id+" name :"+name+" salary :"+salary;
    }
    public String getID(){
        return id;
    }
    public String getName(){
        return name;
    }
    public double getSalary(){
        return salary;
    }
    public static void showNum(){
        System.out.println(count);
    }
}
