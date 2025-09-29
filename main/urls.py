from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments_list, name='departments_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('specialties/', views.specialties_list, name='specialties_list'),
    path('specialties/<int:pk>/', views.specialty_detail, name='specialty_detail'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]