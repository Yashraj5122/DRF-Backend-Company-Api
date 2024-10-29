from rest_framework import serializers
from .models import *
from django.utils import timezone

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['created_at','updated_at','is_deleted']
    
    def validate_comp_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Company name cannot be blank.")
        return value

class BranchSerializer(serializers.ModelSerializer):
    comp_code = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    class Meta:
        model = Branch
        exclude = ['created_at','updated_at','is_deleted']

    def validate(self,data):
        branch_name = data.get('branch_name')
        comp_code = data.get('comp_code')
        if Branch.objects.filter(branch_name=branch_name, comp_code=comp_code,is_deleted=False).exists():
            raise serializers.ValidationError("Branch name must be unique within the same company.")
        return data

class EmployeeSerializer(serializers.ModelSerializer): 
    comp_code = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())  
    branch_code = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    class Meta:
        model = Employee
        exclude = ['created_at','updated_at','is_deleted']

    def validate_emp_email(self, value):
        if Employee.objects.filter(emp_email=value, is_deleted=False).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value
        
    def validate_emp_doj(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date of Joining cannot be in future.")
        return value