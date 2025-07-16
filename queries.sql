
-- Common queries for Health Management System

-- 1. Get all patients
SELECT * FROM patients ORDER BY name;

-- 2. Get all doctors
SELECT * FROM doctors ORDER BY name;

-- 3. Find patients by age range
SELECT * FROM patients WHERE age BETWEEN 30 AND 60;

-- 4. Find doctors by specialization
SELECT * FROM doctors WHERE specialization = 'Cardiology';

-- 5. Count patients by diagnosis
SELECT diagnosis, COUNT(*) as patient_count 
FROM patients 
GROUP BY diagnosis 
ORDER BY patient_count DESC;

-- 6. Get average age of patients
SELECT AVG(age) as average_age FROM patients;

-- 7. Find oldest and youngest patients
SELECT 
    MIN(age) as youngest_patient,
    MAX(age) as oldest_patient
FROM patients;

-- 8. Search patients by name
SELECT * FROM patients WHERE name LIKE '%John%';

-- 9. Get patient statistics
SELECT 
    COUNT(*) as total_patients,
    AVG(age) as average_age,
    MIN(age) as youngest,
    MAX(age) as oldest
FROM patients;

-- 10. Get doctors count by specialization
SELECT 
    specialization,
    COUNT(*) as doctor_count
FROM doctors
GROUP BY specialization
ORDER BY doctor_count DESC;

-- 11. Recent patients (last 30 days)
SELECT * FROM patients 
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY);

-- 12. Health summary view
SELECT 
    p.diagnosis,
    COUNT(*) as cases,
    AVG(p.age) as avg_age,
    MIN(p.age) as min_age,
    MAX(p.age) as max_age
FROM patients p
GROUP BY p.diagnosis
ORDER BY cases DESC;
