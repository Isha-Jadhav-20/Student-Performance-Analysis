CREATE DATABASE student_performance;
USE student_performance;

CREATE TABLE students (

    Student_ID INT,
    school VARCHAR(10),
    sex VARCHAR(10),
    age INT,
    address VARCHAR(10),
    famsize VARCHAR(10),
    Pstatus VARCHAR(10),
    Medu INT,
    Fedu INT,
    Mjob VARCHAR(50),
    Fjob VARCHAR(50),
    reason VARCHAR(50),
    guardian VARCHAR(50),
    traveltime INT,
    studytime INT,
    failures INT,
    schoolsup VARCHAR(10),
    famsup VARCHAR(10),
    paid VARCHAR(10),
    activities VARCHAR(10),
    nursery VARCHAR(10),
    higher VARCHAR(10),
    internet VARCHAR(10),
    romantic VARCHAR(10),
    famrel INT,
    freetime INT,
    goout INT,
    Dalc INT,
    Walc INT,
    health INT,
    absences INT,
    G1 INT,
    G2 INT,
    G3 INT,
    Total_Marks INT,
    Average_Marks FLOAT,
    Percentage FLOAT,
    Result VARCHAR(10),
    Parental_Education_Score INT,
    Parental_Education VARCHAR(50),
    Study_Hours_Category VARCHAR(50),
    Student_Rank INT
);

-- 1) Count Total Students

SELECT COUNT(*) AS Total_Students FROM students;

-- 2) Calculate Average Marks

SELECT AVG(Average_Marks) AS Average_Marks FROM students;

-- 3) Find Top 10 Performing Students

SELECT
    Student_ID,
    Total_Marks,
    Percentage
FROM students
ORDER BY Total_Marks DESC
LIMIT 10;

-- 4) Gender-wise Performance

SELECT
    sex,
    AVG(Average_Marks) AS Average_Marks
FROM students
GROUP BY sex;

-- 5) Calculate Average Absences

SELECT AVG(absences) AS Average_Absences
FROM students;

-- 6) Find Students Scoring Above 90 Percent

SELECT
    Student_ID,
    Percentage
FROM students
WHERE Percentage > 90;

-- 7) Analyze Performance by Parental Education

SELECT
    Parental_Education,
    AVG(Average_Marks) AS Average_Marks
FROM students
GROUP BY Parental_Education;

-- 8) Rank Students Based on Total Marks

SELECT
    Student_ID,
    Total_Marks,
    RANK() OVER (
        ORDER BY Total_Marks DESC
    ) AS Rank_Number
FROM students;

-- 9) Find Average Study Time

SELECT AVG(studytime) AS Average_Study_Time FROM students;

-- 10) Pass and Fail Percentage

SELECT
    Result,
    COUNT(*) AS Student_Count,
    ROUND(
        COUNT(*) * 100.0 /(SELECT COUNT(*) FROM students),2
    ) AS Percentage
FROM students
GROUP BY Result;