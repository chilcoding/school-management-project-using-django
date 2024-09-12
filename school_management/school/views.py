from django.shortcuts import render
from .models import Student, Teacher, Course

def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    return render(request, 'school/index.html', {'students': students, 'teachers': teachers, 'courses': courses})
