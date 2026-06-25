public class Enum_ {
    public static void main(String[] args) {
        final char grade1 = 'A';
        final char grade2 = 'B';
        char myGrade = 'M'; //invalid I dont want this
        System.out.println(myGrade);

        Grade my_grade = Grade.A;
        System.out.println(my_grade+" "+my_grade.getPoint());
        Name name = Name.mitta;
        System.out.printf("hey girl I am %s %.2f oh your duck %s%n",name,name.size,name.description);
        for(Grade i:Grade.values()){
            System.out.println(i);
        }

    }

}
// enum สร้างนอก class
enum Name {
  
    sky(54,"It's big"),podduang(0,"it's baby na"),mitta(38,"god bless you man");
    final double size;
    final String description;
    private Name(double size,String des){
        this.size = size;
        this.description = des;
    }

    
}
enum Grade {
    A, B, C, D, F;
    //method enum
    double getPoint(){
        switch (this) {
            case A:
                return 4.0;
            case B:
                return 3.0;
            case C:
                return 2.0;
            case D:
                return 1.0;
            default: return 0.0;
        }
    }
}
