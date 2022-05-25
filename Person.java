public class Person{
    
    private String name;
    private String SSN;
    private int Age;
    private String Gender;
    private String Address;
    private String Telephonenumber;

    public Person(String name, String SSN, int Age, String Gender, String Address, String Telephonenumber){
        
        this.name = name;
        this.SSN = SSN;
        this.Age = Age;
        this.Gender = Gender;
        this.Address = Address;
        this.Telephonenumber = Telephonenumber;
    }

    public String getname(){
        return this.name;
    }

    public String getSSN(){
        return this.SSN;
    }

    public int getAge(){
        return this.Age;
    }

    public String getGender(){
        return this.Gender;
    }

    public String getAddress(){
        return this.Address;
    }

    public String getTelephonenumber(){
        return this.Telephonenumber;
    }

    public String toString(){
        
        return getname() + ", social security number is: " +getSSN() + " and " + getAge()+ " years old, gender is  " + getGender()+ ", live at "+ getAddress()+ ". Phone number is " + getTelephonenumber();
        
    }
}