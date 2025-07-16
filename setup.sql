-- Create database
CREATE DATABASE IF NOT EXISTS health_system;
USE health_system;

-- Create patients table
CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    diagnosis VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create doctors table
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO patients (name, age, diagnosis) VALUES
('John Doe', 45, 'Hypertension'),
('Jane Smith', 32, 'Diabetes'),
('Bob Johnson', 28, 'Flu'),
('Alice Brown', 55, 'Arthritis'),
('Charlie Davis', 67, 'Heart Disease');

INSERT INTO doctors (name, specialization) VALUES
('Dr. Wilson', 'Cardiology'),
('Dr. Anderson', 'Internal Medicine'),
('Dr. Thompson', 'Pediatrics'),
('Dr. Garcia', 'Orthopedics'),
('Dr. Miller', 'General Practice');

-- Create indexes for better performance
CREATE INDEX idx_patient_name ON patients(name);
CREATE INDEX idx_doctor_specialization ON doctors(specialization);
