import java.text.DecimalFormat;

public class Professional extends Employee2{
    
    public double monthlysalary;
    
    private final int days_of_vacation_earned_that_week = 2;
    private double weeklysalary;
    private double weekly_amount_contributed_for_health_insurance;
    private static final DecimalFormat df = new DecimalFormat("0.00");

    
    
    
    public Professional(String name, String SSN, int Age, String Gender, String Address, String Telephonenumber,String department, String jobtitle, int yearofhire, int hoursworked_weekly, double monthlysalary){

        super(name,SSN,Age,Gender,Address,Telephonenumber,department,jobtitle,yearofhire,hoursworked_weekly);
        
        this.monthlysalary = monthlysalary;
        
       
    }    


    
    
    public double getmonthlysalary(){
        return this.monthlysalary;
    }
    
    
    
    public String calculating_weeklysalary(){
        
        
        this.weeklysalary = this.monthlysalary/4.3;
        
        return df.format(this.weeklysalary);
    }

    public double computing_health_care_contributions(){
        
        if(hoursworked_weekly >= 50){
            weekly_amount_contributed_for_health_insurance = 25.55;
        }
    
        else{
            weekly_amount_contributed_for_health_insurance = 15.55;
        }
        return weekly_amount_contributed_for_health_insurance;
    }


    public int vacation_days_earned_that_week(){
        return this.days_of_vacation_earned_that_week;
    }


    
    
    
    public String toString(){
        return "Professional Employee: "  + super.toString() +  "\nMonthly salary is: " + getmonthlysalary() + " CA$ \nWeekly salary is: " + calculating_weeklysalary() + " CA$ \nThe weekly amount contributed for health insurance is: " + computing_health_care_contributions() + " CA$ \nVacation days earned that week: " + vacation_days_earned_that_week();

    }




}