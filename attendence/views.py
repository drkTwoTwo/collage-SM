from django.shortcuts import render, get_object_or_404, redirect
from .models import Class, Student, Assign, AttendanceSession, Attendance, Teacher
from datetime import date
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            request.session['teacher_id'] = teacher_id
            response = redirect('home')
            response.set_cookie('teacher_id', teacher_id, max_age=7 * 24 * 60 * 60)
            return response
        except Teacher.DoesNotExist:
            return HttpResponse('Invalid Teacher ID')
    return render(request,'login.html')

def home(request):
    if 'teacher_id' not in request.session:
        teacher_id = request.COOKIES.get('teacher_id')
        if teacher_id:
            request.session['teacher_id'] = teacher_id
        else:
            return redirect('login_view')
    return render(request, 'home.html')

def preAttend(request):
    if 'teacher_id' not in request.session:
        return redirect('login_view')
    return render(request, 'preAttend.html')
    return render(request, 'login.html')
    
def logout_view(request):
    request.session.flush()
    response = redirect('login_view')
    response.delete_cookie('teacher_id')
    return response

def attendance_view(request, class_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login_view')
    class_obj = get_object_or_404(Class, id=class_id)
    assigns = Assign.objects.filter(teacher_id=teacher_id, class_id=class_id)
    if not assigns.exists():
        return redirect('home')
    if assigns.count() > 1 and 'assign_course' not in request.GET:
        return redirect('select_assign_view', class_id=class_id)
    assign = assigns.first() if assigns.count() == 1 else get_object_or_404(Assign, course=request.GET.get('assign_course'), teacher=teacher_id)
    session, _ = AttendanceSession.objects.get_or_create(
        assign=assign,
        date=date.today(),
        defaults={'day': date.today().weekday()}
    )
    students = Student.objects.filter(class_id=class_obj)
    if request.method == "POST":
        for student in students:
            status = request.POST.get(f"attendance_{student.roll}", 'off') == 'on'
            Attendance.objects.update_or_create(
                session=session,
                student=student,
                defaults={'status': status}
            )
        return redirect('home')
    return render(request, 'attend.html', {
        'students': students,
        'class_obj': class_obj,
        'teacher_id': teacher_id,
        'assign': assign,
        'session': session,
    })

def select_assign_view(request, class_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login_view')
    class_obj = get_object_or_404(Class, id=class_id)
    assigns = Assign.objects.filter(teacher_id=teacher_id, class_id=class_id)
    if request.method == "POST":
        assign_course = request.POST.get('assign_course')
        return redirect(f'/attendance/{class_id}/?assign_course={assign_course}')
    return render(request, 'select_course.html', {
        'class_obj': class_obj,
        'assigns': assigns
    })

def student_attendance(request):
    student = None
    attendance_data = []
    if request.method == "GET":
        roll_number = request.GET.get('roll_number')
        if roll_number:
            student = get_object_or_404(Student, roll=roll_number)
            assigns = Assign.objects.filter(class_id=student.class_id)
            for assign in assigns:
                total_classes = AttendanceSession.objects.filter(assign=assign).count()
                attended_classes = Attendance.objects.filter(
                    student=student,
                    session__assign=assign,
                    status=True
                ).count()
                attendance_percentage = (attended_classes / total_classes) * 100 if total_classes > 0 else 0
                attendance_data.append({
                    'course_name': assign.course,
                    'total_classes': total_classes,
                    'attended_classes': attended_classes,
                    'percentage': round(attendance_percentage, 2),
                    'percentage_absent': round(100 - attendance_percentage, 2)
                })
    return render(request, 'atten_search.html', {
        'student': student,
        'attendance_data': attendance_data
    })
