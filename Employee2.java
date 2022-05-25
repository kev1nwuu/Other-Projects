public abstract class Employee2 extends Person{

   
    private String department;
    private String jobtitle;
    private int yearofhire;
    public int hoursworked_weekly;
    
    
    public Employee2(String name, String SSN, int Age, String Gender, String Address, String Telephonenumber,String department, String jobtitle, int yearofhire, int hoursworked_weekly){
        
        super(name,SSN,Age,Gender,Address,Telephonenumber);
        
        this.hoursworked_weekly = hoursworked_weekly;
        this.department = department;
        this.jobtitle = jobtitle;
        this.yearofhire = yearofhire;
    }

    public int gethoursworked_weekly(){
        return this.hoursworked_weekly;
    }
    
    
    public String getdepartment(){
        return this.department;
    }

    public String getjobtitle(){
        return this.jobtitle;
    }

    public int getyearofhire(){
        return this.yearofhire;
    }

    public abstract String calculating_weeklysalary();
    
    public abstract double computing_health_care_contributions();
    
    public abstract int vacation_days_earned_that_week();
    
    
    
    
    
    public String toString(){
        
        return super.toString() + ".\nWorking on: " + getdepartment() +"\nJobtitle is: " + getjobtitle()+ "\nYear of hire is: "+ getyearofhire()+"\nhours worked weekly is: " + gethoursworked_weekly();
    }


}



