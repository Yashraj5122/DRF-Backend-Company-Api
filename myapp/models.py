from django.db import models
from django.utils import timezone

class Company(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    comp_code = models.AutoField(primary_key=True)
    comp_name = models.CharField(max_length=255)
    comp_location = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class Branch(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    branch_code = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    comp_code = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class Employee(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    emp_id = models.AutoField(primary_key=True)
    emp_designation = models.CharField(max_length = 255, null = True, blank = True)
    emp_email = models.EmailField(unique = True)
    emp_doj = models.DateField()

    dept_choices = [
        ('HR', 'Human Resources'),
        ('FIN', 'Finance'),
        ('DEV', 'Developers'),
        ('DES', 'Design')
    ]

    emp_dept = models.CharField(max_length=3, choices=dept_choices, null=True, blank=True)
    comp_code = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_code = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()