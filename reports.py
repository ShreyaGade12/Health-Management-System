import mysql.connector
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='health_system'
        )
        self.cursor = self.conn.cursor()
    
    def patient_report(self, patient_id=None):
        if patient_id:
            query = "SELECT * FROM patients WHERE id = %s"
            self.cursor.execute(query, (patient_id,))
        else:
            query = "SELECT * FROM patients"
            self.cursor.execute(query)
        
        patients = self.cursor.fetchall()
        
        print("=== PATIENT REPORT ===")
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
        
        for patient in patients:
            print(f"ID: {patient[0]}")
            print(f"Name: {patient[1]}")
            print(f"Age: {patient[2]}")
            print(f"Diagnosis: {patient[3]}")
            print("-" * 30)
    
    def doctor_report(self):
        query = "SELECT * FROM doctors"
        self.cursor.execute(query)
        doctors = self.cursor.fetchall()
        
        print("=== DOCTOR REPORT ===")
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
        
        for doctor in doctors:
            print(f"ID: {doctor[0]}")
            print(f"Name: {doctor[1]}")
            print(f"Specialization: {doctor[2]}")
            print("-" * 30)
    
    def health_summary(self):
        # Get total counts
        self.cursor.execute("SELECT COUNT(*) FROM patients")
        total_patients = self.cursor.fetchone()[0]
        
        self.cursor.execute("SELECT COUNT(*) FROM doctors")
        total_doctors = self.cursor.fetchone()[0]
        
        # Get age statistics
        self.cursor.execute("SELECT AVG(age), MIN(age), MAX(age) FROM patients")
        age_stats = self.cursor.fetchone()
        
        # Get common diagnoses
        self.cursor.execute("SELECT diagnosis, COUNT(*) as count FROM patients GROUP BY diagnosis ORDER BY count DESC LIMIT 5")
        common_diagnoses = self.cursor.fetchall()
        
        print("=== HEALTH SYSTEM SUMMARY ===")
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
        print(f"Total Patients: {total_patients}")
        print(f"Total Doctors: {total_doctors}")
        if age_stats[0]:
            print(f"Average Patient Age: {age_stats[0]:.1f} years")
            print(f"Age Range: {age_stats[1]} - {age_stats[2]} years")
        
        print("\nTop Diagnoses:")
        for diagnosis, count in common_diagnoses:
            print(f"- {diagnosis}: {count} cases")
    
    def save_report_to_file(self, report_type, filename=None):
        if not filename:
            filename = f"{report_type}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, 'w') as f:
            # Redirect print output to file
            import sys
            original_stdout = sys.stdout
            sys.stdout = f
            
            if report_type == 'patient':
                self.patient_report()
            elif report_type == 'doctor':
                self.doctor_report()
            elif report_type == 'summary':
                self.health_summary()
            
            sys.stdout = original_stdout
        
        print(f"Report saved to: {filename}")

if __name__ == "__main__":
    reports = ReportGenerator()
    
    # Generate all reports
    reports.patient_report()
    print("\n")
    reports.doctor_report()
    print("\n")
    reports.health_summary()
    
    # Save summary to file
    reports.save_report_to_file('summary')
