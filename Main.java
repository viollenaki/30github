abstract class Employee {
    String name;
    int id;
    double base;

    public Employee(String name, int id, double base) {
        this.name = name;
        this.id = id;
        this.base = base;
    }

    public abstract double calculateSalary();

    public void displayEmployeeInfo() {
        System.out.println("Employee ID--- " + id);
        System.out.println("Name--- " + name);
        System.out.println("Salary--- " + calculateSalary());
    }
}

interface Payable {
    double getPaymentAmount();
}

class FullTimeEmployee extends Employee implements Payable {


    public FullTimeEmployee(String name, int id, double base) {
        super(name, id, base*1.2);    
    }

    @Override
    public double calculateSalary() {
        return base; 
    }

    @Override
    public double getPaymentAmount() {
        return calculateSalary();
    }
}

class ContractEmployee extends Employee implements Payable {
    private double hourly;
    private int hours;

    public ContractEmployee(String name, int id, double hourly, int hours) {
        super(name, id, 0); 
        this.hourly = hourly;
        this.hours = hours;
    }

    @Override
    public double calculateSalary() {
        return hourly * hours;
    }

    @Override
    public double getPaymentAmount() {
        return calculateSalary();
    }
}

public class Main {
    public static void main(String[] args) {
        Employee[] employees = new Employee[2];
        employees[0] = new FullTimeEmployee("Emil", 1, 10000);
        employees[1] = new ContractEmployee("Akbar", 2, 20, 40);
        for (Employee e : employees){
            e.displayEmployeeInfo();
            System.out.println("payment Amount--- " + e.calculateSalary());
        }
    }
}
