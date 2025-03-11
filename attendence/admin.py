from django.contrib import admin
from .models import Dept, Course, Class, Student, Teacher, Assign, AttendanceSession, Attendance

admin.site.register(Dept)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assign)
admin.site.register(AttendanceSession)
admin.site.register(Attendance)
