import java.util.*;

public class Main {
    private static Database db = new Database();
    private static Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        db.connect();
        
        while (true) {
            showMenu();
            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline
            
            switch (choice) {
                case 1:
                    addPatient();
                    break;
                case 2:
                    viewPatients();
                    break;
                case 3:
                    addDoctor();
                    break;
                case 4:
                    viewDoctors();
                    break;
                case 5:
                    System.out.println("Goodbye!");
                    return;
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
    
    private static void showMenu() {
        System.out.println("\n=== Health Management System ===");
        System.out.println("1. Add Patient");
        System.out.println("2. View Patients");
        System.out.println("3. Add Doctor");
        System.out.println("4. View Doctors");
        System.out.println("5. Exit");
        System.out.print("Choose option: ");
    }
    
    private static void addPatient() {
        System.out.print("Enter patient name: ");
        String name = scanner.nextLine();
        System.out.print("Enter age: ");
        int age = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Enter diagnosis: ");
        String diagnosis = scanner.nextLine();
        
        Patient patient = new Patient(name, age, diagnosis);
        db.addPatient(patient);
        System.out.println("Patient added successfully!");
    }
    
    private static void viewPatients() {
        List<Patient> patients = db.getAllPatients();
        System.out.println("\n=== Patients ===");
        for (Patient p : patients) {
            System.out.println(p.toString());
        }
    }
    
    private static void addDoctor() {
        System.out.print("Enter doctor name: ");
        String name = scanner.nextLine();
        System.out.print("Enter specialization: ");
        String specialization = scanner.nextLine();
        
        Doctor doctor = new Doctor(name, specialization);
        db.addDoctor(doctor);
        System.out.println("Doctor added successfully!");
    }
    
    private static void viewDoctors() {
        List<Doctor> doctors = db.getAllDoctors();
        System.out.println("\n=== Doctors ===");
        for (Doctor d : doctors) {
            System.out.println(d.toString());
        }
    }
}
