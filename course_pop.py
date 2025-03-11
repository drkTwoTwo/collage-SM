from your_app.models import Course, Dept

# Ensure you have a 'CSE' department
cse_dept, created = Dept.objects.get_or_create(name="CSE")

# Course data
courses = [
    ("COPC-301", "Computer Architecture and Organization"),
    ("COPC-302", "Programming in C"),
    ("COPC-303", "Software Engineering"),
    ("COPC-304", "Hardware and Networking"),
    ("COPC-305", "Database Management System"),
    ("COPC-306", "Programming in C Lab"),
    ("COPC-307", "Hardware and Networking Lab"),
    ("COPC-308", "Database Management System Lab"),
    ("COPC-309", "Internet and Web Technology"),
    ("COPC-310", "Internet and Web Technology Lab"),
    ("OE-303", "Data Visualization and Analysis with Excel (IS)"),
    ("AU-01", "Essence of Indian Knowledge and Tradition"),
    ("COPC-401", "Operating System"),
    ("COPC-402", "Object Oriented Programming with C++"),
    ("COPC-403", "Data Structure using C"),
    ("COPC-404", "Digital Electronics"),
    ("COPC-405", "Operating System Lab"),
    ("COPC-406", "Object Oriented Programming with C++ Lab"),
    ("COPC-407", "Data Structure using C Lab"),
    ("COPE-401", "Multimedia Technology"),
    ("COPE-402", "Scripting Language (Python)"),
    ("OE-401", "Visual Programming"),
    ("OE-402", "Complete UNIX & LINUX OS Fundamentals Training (IS)"),
    ("SI-01", "Internship"),
    ("PR-01", "Minor Project"),
    ("SE-01", "Seminar/Guest Lecture/remedial"),
    ("COPC-501", "Computer Communication and Networking"),
    ("COPC-502", "Basics of Cloud computing"),
    ("COPC-503", "Java Programming"),
    ("COPC-504", "Java Programming Lab"),
    ("COPE-501", "VLSI"),
    ("COPE-502", "VLSI Lab"),
    ("COPE-503", "Data Warehousing and Data Mining"),
    ("COPE-504", "Data Warehousing and Data Mining Lab"),
    ("COPE-505", "Microprocessor and Interfacing"),
    ("COPE-506", "Microprocessor and Interfacing Lab"),
    ("COPE-507", "Applied Mathematics"),
    ("OE-501", "Artificial Intelligence"),
    ("OE-502", "Android Programming"),
    ("OE-503", "Future Technology (IS)"),
    ("OE-504", "Fundamentals of Machine Learning"),
    ("PR-02", "Major Project"),
    ("COPC-601", "Fundamentals of Machine Learning"),
    ("COPC-602", "Information Security"),
    ("COPC-603", "Mobile Computing"),
    ("COPC-604", "Fundamentals of Machine Learning Lab"),
    ("COPC-605", "Information Security Lab"),
    ("OE-601", "Industrial Robotics (TATA)"),
    ("OE-602", "Fundamentals of Data Analysis and Cloud Computing"),
    ("COHSC-601", "Entrepreneurship and Startup"),
    ("SI-02", "Internship"),
    ("PR-03", "Major Project"),
    ("AU-02", "Constitution of India"),
    ("SE-02", "Seminar/DIY lab/Guest Lecture/remedial"),
]

# Bulk insert courses
Course.objects.bulk_create([
    Course(dept=cse_dept, id=course_id, name=course_name)
    for course_id, course_name in courses
])

print("Courses added successfully!")
