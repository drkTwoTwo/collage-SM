from attendence.models import Student,Class


Class_id, created = Class.objects.get_or_create(id="CSE6")
roll_no = [ 
"Nal/22/cs/022","Nal/22/cs/023", "Nal/22/cs/024", "Nal/22/cs/030", "Nal/22/cs/033" ]


# Bulk insert courses
Student.objects.bulk_create([
    Student(class_id=Class_id, roll=Roll)
    for  Roll in roll_no
])

print("Students added successfully!")
