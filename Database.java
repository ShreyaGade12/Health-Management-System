import java.sql.*;
import java.util.*;

public class Database {
    private Connection conn;
    private final String DB_URL = "jdbc:mysql://localhost:3306/health_system";
    private final String USER = "root";
    private final String PASS = "password";
    
    public void connect() {
        try {
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Database connected successfully!");
        } catch (SQLException e) {
            System.out.println("Database connection failed: " + e.getMessage());
        }
    }
    
    public void addPatient(Patient patient) {
        String sql = "INSERT INTO patients (name, age, diagnosis) VALUES (?, ?, ?)";
        try {
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, patient.getName());
            stmt.setInt(2, patient.getAge());
            stmt.setString(3, patient.getDiagnosis());
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error adding patient: " + e.getMessage());
        }
    }
    
    public List<Patient> getAllPatients() {
        List<Patient> patients = new ArrayList<>();
        String sql = "SELECT * FROM patients";
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            
            while (rs.next()) {
                Patient patient = new Patient(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getInt("age"),
                    rs.getString("diagnosis")
                );
                patients.add(patient);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving patients: " + e.getMessage());
        }
        return patients;
    }
    
    public void addDoctor(Doctor doctor) {
        String sql = "INSERT INTO doctors (name, specialization) VALUES (?, ?)";
        try {
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, doctor.getName());
            stmt.setString(2, doctor.getSpecialization());
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error adding doctor: " + e.getMessage());
        }
    }
    
    public List<Doctor> getAllDoctors() {
        List<Doctor> doctors = new ArrayList<>();
        String sql = "SELECT * FROM doctors";
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            
            while (rs.next()) {
                Doctor doctor = new Doctor(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("specialization")
                );
                doctors.add(doctor);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving doctors: " + e.getMessage());
        }
        return doctors;
    }
}
