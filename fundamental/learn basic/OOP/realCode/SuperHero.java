/**
 * SuperHero
 */
public abstract class SuperHero {
    private String name;
    private int age;
    private String job;
    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setJob(String job){
        this.job = job;
    }
    public abstract void ability();
    public String toString(){
        return name + " age " + age + " job "+job; 
    }
}
