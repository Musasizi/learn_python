Class Person{

    //Instance Variables
    private String name = "";
    private int age = 0;
    private String country = "";

    //Constructor
    Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    //Getter
    public String getName (){
        return this.name;
    }
    
    //Setter
    public void setName(String name){
        this.name = name;
    }
}