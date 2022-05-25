import java.text.DecimalFormat;

public class Nonprofessional extends Employee2{

    private double hourlyrate;
    
    
    
    private int days_of_vacation_earned_that_week;
    
    private final double hourly_amount_contributed_for_health_insurance = 0.4; // 0.4 CA$
    private static final DecimalFormat df = new DecimalFormat("0.00");
    
    
    
    public Nonprofessional(String name, String SSN, int Age, String Gender, String Address, String Telephonenumber,String department, String jobtitle, int yearofhire, int hoursworked_weekly, double hourlyrate){
        
        super(name, SSN, Age, Gender, Address, Telephonenumber, department, jobtitle, yearofhire,hoursworked_weekly);
    
        this.hourlyrate = hourlyrate;
    }


    public double gethourlyrate(){
        return this.hourlyrate;
    }

    public String calculating_weeklysalary(){
        
        

        return df.format(hoursworked_weekly*hourlyrate);     
        
        
    }

    public double computing_health_care_contributions(){
        
        double weekly_amount_contributed_for_health_insurance = hoursworked_weekly*hourly_amount_contributed_for_health_insurance;


        return Math.round((weekly_amount_contributed_for_health_insurance*100.0)/100.0);
        
    }

    
    
    public int vacation_days_earned_that_week(){
        
        
        if(hoursworked_weekly >= 45){           ///////// only when the working hours more 45 hours can get vacation_days.
            days_of_vacation_earned_that_week = 1;
        }    
    
        return days_of_vacation_earned_that_week;
    
    }


    public String toString(){
        return "NonProfessional Employee: "  + super.toString() + "\nHourlyrate: " + gethourlyrate() + "\nWeekly salary is: " + calculating_weeklysalary() + " CA$ \nThe weekly amount contributed for health insurance is: " + computing_health_care_contributions() + " CA$ \nVacation days earned that week: " + vacation_days_earned_that_week();

    }



}