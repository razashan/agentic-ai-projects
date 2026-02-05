
import sqlite3
import datetime
import random

db_path = 'datatechcon.db'

def setup_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing tables if they exist (to ensure fresh start)
    cursor.execute("DROP TABLE IF EXISTS sessions")
    cursor.execute("DROP TABLE IF EXISTS enrollments")
    cursor.execute("DROP TABLE IF EXISTS courses")
    cursor.execute("DROP TABLE IF EXISTS instructors")
    cursor.execute("DROP TABLE IF EXISTS learners")

    # Create Tables
    cursor.execute("""
    CREATE TABLE learners (
        learner_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        country TEXT,
        signup_date DATE
    );
    """)

    cursor.execute("""
    CREATE TABLE instructors (
        instructor_id INTEGER PRIMARY KEY,
        name TEXT,
        expertise TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE courses (
        course_id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT,
        price REAL,
        instructor_id INTEGER,
        FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        learner_id INTEGER,
        course_id INTEGER,
        enrollment_date DATE,
        FOREIGN KEY (learner_id) REFERENCES learners(learner_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE sessions (
        session_id INTEGER PRIMARY KEY,
        learner_id INTEGER,
        course_id INTEGER,
        session_date DATE,
        duration_minutes INTEGER,
        FOREIGN KEY (learner_id) REFERENCES learners(learner_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    );
    """)

    # Populate Sample Data
    
    # Intructors
    instructors = [
        (1, "Alice Johnson", "Data Science"),
        (2, "Bob Smith", "Web Development"),
        (3, "Carol Williams", "Machine Learning"),
        (4, "David Brown", "Cloud Computing")
    ]
    cursor.executemany("INSERT INTO instructors VALUES (?, ?, ?)", instructors)

    # Courses
    courses = [
        (101, "Intro to Python", "Programming", 49.99, 1),
        (102, "Advanced SQL", "Data Science", 59.99, 1),
        (103, "Web Dev Bootcamp", "Web Development", 99.99, 2),
        (104, "React for Beginners", "Web Development", 69.99, 2),
        (105, "Machine Learning A-Z", "Machine Learning", 129.99, 3),
        (106, "Deep Learning Specialization", "Machine Learning", 149.99, 3),
        (107, "AWS Solutions Architect", "Cloud Computing", 199.99, 4),
        (108, "Google Cloud Fundamentals", "Cloud Computing", 89.99, 4)
    ]
    cursor.executemany("INSERT INTO courses VALUES (?, ?, ?, ?, ?)", courses)

    # Learners and Enrollments
    # Generate 50 learners
    learners = []
    enrollments = []
    sessions = []
    
    countries = ["USA", "UK", "Canada", "Germany", "India", "Australia", "France"]
    
    for i in range(1, 51):
        name = f"Learner_{i}"
        email = f"learner_{i}@example.com"
        country = random.choice(countries)
        signup_date = (datetime.date(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 365))).isoformat()
        learners.append((i, name, email, country, signup_date))
        
        # Enroll in 1-3 courses
        num_courses = random.randint(1, 3)
        enrolled_courses = random.sample(courses, num_courses)
        
        for course in enrolled_courses:
            enrollment_id = len(enrollments) + 1
            enrollment_date = (datetime.date.fromisoformat(signup_date) + datetime.timedelta(days=random.randint(0, 30))).isoformat()
            enrollments.append((enrollment_id, i, course[0], enrollment_date))
            
            # Create some sessions for this enrollment
            for _ in range(random.randint(1, 5)):
                session_id = len(sessions) + 1
                session_date = (datetime.date.fromisoformat(enrollment_date) + datetime.timedelta(days=random.randint(1, 10))).isoformat()
                duration = random.randint(15, 120)
                sessions.append((session_id, i, course[0], session_date, duration))

    cursor.executemany("INSERT INTO learners VALUES (?, ?, ?, ?, ?)", learners)
    cursor.executemany("INSERT INTO enrollments VALUES (?, ?, ?, ?)", enrollments)
    cursor.executemany("INSERT INTO sessions VALUES (?, ?, ?, ?, ?)", sessions)

    conn.commit()
    conn.close()
    print("Database 'datatechcon.db' setup complete with schema and sample data.")

if __name__ == "__main__":
    setup_database()
