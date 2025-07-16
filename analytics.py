import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

class HealthAnalytics:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='health_system'
        )
    
    def get_patient_data(self):
        query = "SELECT * FROM patients"
        df = pd.read_sql(query, self.conn)
        return df
    
    def age_distribution(self):
        df = self.get_patient_data()
        plt.figure(figsize=(10, 6))
        plt.hist(df['age'], bins=20, edgecolor='black')
        plt.title('Patient Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Number of Patients')
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def diagnosis_analysis(self):
        df = self.get_patient_data()
        diagnosis_counts = df['diagnosis'].value_counts()
        
        plt.figure(figsize=(12, 6))
        diagnosis_counts.plot(kind='bar')
        plt.title('Most Common Diagnoses')
        plt.xlabel('Diagnosis')
        plt.ylabel('Number of Cases')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        return diagnosis_counts
    
    def patient_statistics(self):
        df = self.get_patient_data()
        stats = {
            'total_patients': len(df),
            'average_age': df['age'].mean(),
            'age_range': (df['age'].min(), df['age'].max()),
            'most_common_diagnosis': df['diagnosis'].mode()[0] if not df.empty else 'None'
        }
        return stats
    
    def generate_summary(self):
        stats = self.patient_statistics()
        print("=== Health System Analytics ===")
        print(f"Total Patients: {stats['total_patients']}")
        print(f"Average Age: {stats['average_age']:.1f} years")
        print(f"Age Range: {stats['age_range'][0]} - {stats['age_range'][1]} years")
        print(f"Most Common Diagnosis: {stats['most_common_diagnosis']}")

if __name__ == "__main__":
    analytics = HealthAnalytics()
    analytics.generate_summary()
    analytics.age_distribution()
    analytics.diagnosis_analysis()
