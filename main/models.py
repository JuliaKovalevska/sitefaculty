from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    head = models.CharField(max_length=200, blank=True, null=True)
    office = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    coordinator_name = models.CharField(max_length=200, blank=True, null=True)
    coordinator_contact = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='specialties')
    disciplines = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name