# Health Management System

A comprehensive health management system built with Java, Python, and SQL for managing patients, doctors, and health analytics.

## 🚀 Features

- **Patient Management**: Add, view, and manage patient records
- **Doctor Management**: Maintain doctor profiles and specializations
- **Health Analytics**: Generate insights and visualizations from health data
- **Reporting System**: Create detailed reports for patients and doctors
- **Web Interface**: Simple and intuitive web-based dashboard

## 🛠️ Technology Stack

- **Backend**: Java (Core Java, JDBC)
- **Analytics**: Python (pandas, matplotlib, mysql-connector)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Visualization**: Chart.js, matplotlib

## 📁 Project Structure

```
health-system/
├── java/
│   ├── Main.java              # Main application entry point
│   ├── Patient.java           # Patient data model
│   ├── Doctor.java            # Doctor data model
│   └── Database.java          # Database connection handler
├── python/
│   ├── analytics.py           # Health data analysis
│   └── reports.py             # Report generation
├── sql/
│   ├── setup.sql              # Database schema and sample data
│   └── queries.sql            # Common database queries
├── web/
│   ├── index.html             # Web interface
│   └── style.css              # Styling
└── README.md                  # Project documentation
```

## 🔧 Prerequisites

- **Java**: JDK 8 or higher
- **Python**: Python 3.7+
- **MySQL**: MySQL 5.7 or higher
- **JDBC Driver**: MySQL Connector/J

### Python Dependencies
```bash
pip install mysql-connector-python pandas matplotlib
```

## 🚀 Installation & Setup

### 1. Database Setup
```sql
-- Run setup.sql to create database and tables
mysql -u root -p < sql/setup.sql
```

### 2. Configure Database Connection
Update database credentials in:
- `java/Database.java`
- `python/analytics.py`
- `python/reports.py`

```java
// Database.java
private final String DB_URL = "jdbc:mysql://localhost:3306/health_system";
private final String USER = "your_username";
private final String PASS = "your_password";
```

### 3. Compile and Run Java Application
```bash
cd java/
javac -cp ".:mysql-connector-java-8.0.33.jar" *.java
java -cp ".:mysql-connector-java-8.0.33.jar" Main
```

### 4. Run Python Analytics
```bash
cd python/
python analytics.py
python reports.py
```

### 5. Launch Web Interface
Open `web/index.html` in your browser

## 📊 Usage

### Java Application
The console-based Java application provides:
- Interactive menu system
- Patient registration and management
- Doctor profile management
- Database operations

### Python Analytics
Generate health insights:
```bash
python analytics.py
```
- Patient age distribution
- Diagnosis frequency analysis
- Health statistics summary

### Web Interface
Access the web dashboard for:
- Patient and doctor management
- Real-time analytics
- Visual data representation

## 🔍 Key Components

### Patient Management
- **Add Patient**: Register new patients with personal and medical details
- **View Patients**: Display all registered patients
- **Patient Analytics**: Age distribution and health trends

### Doctor Management
- **Add Doctor**: Register healthcare providers with specializations
- **View Doctors**: List all registered doctors
- **Specialization Analysis**: Track medical specialties

### Analytics & Reporting
- **Health Statistics**: Patient demographics and health metrics
- **Visual Reports**: Charts and graphs for data visualization
- **Export Reports**: Save reports to files

## 🗄️ Database Schema

### Patients Table
```sql
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    diagnosis VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Doctors Table
```sql
CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📈 Analytics Features

- **Age Distribution**: Histogram of patient ages
- **Diagnosis Trends**: Most common health conditions
- **Statistical Summary**: Average age, patient count, etc.
- **Report Generation**: Automated report creation

## 🔒 Security Considerations

- Input validation for all user inputs
- Parameterized queries to prevent SQL injection
- Basic error handling and logging
- Database connection security

## 🚧 Future Enhancements

- [ ] Appointment scheduling system
- [ ] Medical history tracking
- [ ] Prescription management
- [ ] User authentication and authorization
- [ ] REST API development
- [ ] Mobile application support
- [ ] Advanced analytics with machine learning

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify MySQL service is running
   - Check database credentials
   - Ensure database exists

2. **Java Compilation Error**
   - Verify JDBC driver is in classpath
   - Check Java version compatibility

3. **Python Module Error**
   - Install required packages: `pip install -r requirements.txt`
   - Verify Python version

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

 
