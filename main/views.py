from django.shortcuts import render, get_object_or_404
from .models import Department, Specialty, Teacher

def home(request):
    return render(request, 'main/home.html')

def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'main/departments_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'main/department_detail.html', {'department': department})

def specialties_list(request):
    specialties = Specialty.objects.all()
    return render(request, 'main/specialties_list.html', {'specialties': specialties})

def specialty_detail(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    return render(request, 'main/specialty_detail.html', {'specialty': specialty})

def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teachers_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'main/teacher_detail.html', {'teacher': teacher})