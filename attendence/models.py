from django.db import models
from django.contrib.auth.models import User

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)
time_slots = (
		('9:00 - 10:00', '9:00 - 10:00'),
		('10:00 - 11:00', '10:00 - 11:00'),
		('11:00 - 12:00', '11:00 - 12:00'),
		('1:00 - 2:00', '1:00 - 2:00'),
		('2:00 - 3:00', '2:00 - 3:00'),
)
class Dept(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.id

class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Class(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    sem = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f"{self.id} - Semester {self.dept.name}"


class Student(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    roll = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, default="No Name")
    def __str__(self):
        return f"{self.roll}   - {self.class_id.id} -  {self.name}"

class Teacher(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100, null=True, blank=True, default='Unnamed Teacher')


    def __str__(self):
        return f"{self.name} ({self.dept.name})"

class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'class_id', 'teacher'),)

    def __str__(self):
        return f"{self.teacher.name} : {self.course.id} : {self.class_id}"

class AttendanceSession(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    date = models.DateField()
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK, default='Monday')
    period = models.CharField(max_length=50, choices=time_slots, default='9:00 - 10:00')

    def __str__(self):
        return f"{self.assign.course.id} on {self.date} ({self.period})"

class Attendance(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.student.roll} - {'Present' if self.status else 'Absent'}"


