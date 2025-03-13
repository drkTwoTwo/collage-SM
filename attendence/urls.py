from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student-attendance/', views.student_attendance, name='student_attendance'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),  # Ensure this is present
    path('pre-attendance/', views.preAttend, name='preAttend'),
    path('error/<str:result>/', views.err_view, name='err_view'),
    path('attendance/<str:class_id>/', views.attendance_view, name='attendance_view'),
    path('attendance/<str:class_id>/select/', views.select_assign_view, name='select_assign_view'),

]
