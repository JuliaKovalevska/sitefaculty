from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Department, Specialty, Teacher

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if Department.objects.exists():
        return

    dept1 = Department.objects.create(name="Кафедра Комп'ютерних Наук", description="Опис кафедри КН")
    dept2 = Department.objects.create(name="Кафедра Математики", description="Опис кафедри Математики")

    spec1 = Specialty.objects.create(name="Інформатика", description="Опис спеціальності Інформатика")
    spec2 = Specialty.objects.create(name="Прикладна математика", description="Опис спеціальності ПМ")

    Teacher.objects.create(name="Іван Іваненко", bio="Викладач комп'ютерних наук", department=dept1, specialty=spec1)
    Teacher.objects.create(name="Марія Петрова", bio="Викладач математики", department=dept2, specialty=spec2)