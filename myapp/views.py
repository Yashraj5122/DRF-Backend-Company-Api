from rest_framework.decorators import api_view
from .models import *
from .Serializers import *
from rest_framework. response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from .pagination import CustomPagination

# ----------------Company-------------------------#

@csrf_exempt
@api_view(['POST'])
def register_company(request):
    data = request.data

    if isinstance(data,list):
        serializer = CompanySerializer(data=data, many=True)
        if serializer.is_valid():
            company_objects = [Company(**item) for item in serializer.validated_data]
            Company.objects.bulk_create(company_objects)
            return Response({'message' : 'Companies created successfully', 'data' : serializer.data},status=201)
        return Response({'error' : serializer.errors},status=400)
    
    serializer = CompanySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Company added successfully', 'data' : serializer.data}, status=201)
    return Response({'error' : serializer.errors},status=400)

@csrf_exempt
@api_view(['GET'])
def list_company(request):
    companies = Company.objects.filter(is_deleted=False).order_by('comp_code')
    if not companies.exists():
        return Response({'error' : 'No Company details found'})
    
    paginator = CustomPagination()
    paginated_companies = paginator.paginate_queryset(companies,request) 
    serializer = CompanySerializer(paginated_companies, many=True)
    return paginator.get_paginated_response({'message' : 'Companies retrieved successfully', 'data' : serializer.data})

@csrf_exempt
@api_view(['GET'])
def get_company_details(request, comp_code):
    try:
        company = Company.objects.get(comp_code=comp_code, is_deleted=False)
    except Company.DoesNotExist:
        return Response({'error' : 'Company does not exist'}, status=404)
    serializer = CompanySerializer(company)
    return Response({'message' : 'Company retrieved successfully', 'data' : serializer.data})

@csrf_exempt
@api_view(['PUT', 'PATCH'])
def update_company(request):
    data = request.data
    try:
        obj = Company.objects.get(comp_code = data['comp_code'])
        
        if obj.is_deleted:
            return Response({'error' : 'Company has been already been deleted'})
        
    except Company.DoesNotExist:
        return Response({'error' : 'Company Not Found'}, status=404)
    
    if request.method == 'PUT':
        serializer = CompanySerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Company details updated successfully', 'data' : serializer.data})
        return Response({'error' : serializer.errors}, status=400)

    elif request.method == 'PATCH':
        serializer = CompanySerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Company details updated successfully', 'data' : serializer.data})
        return Response({'error' : serializer.errors}, status=400)
    

@csrf_exempt
@api_view(['DELETE'])
def delete_company(request,comp_code):
    try:
        obj = Company.objects.get(comp_code=comp_code)
        if obj.is_deleted:
            return Response({'error' : 'Company has already been deleted'})
    except Company.DoesNotExist:
        return Response({'error' : 'Company Not Found'}, status=404)
    
    obj.soft_delete()
    obj.save()

    return Response({'message' : 'Company deleted Successfully'}, status=200)
    

@csrf_exempt
@api_view(['GET'])
def list_deleted_company(request):
    companies = Company.objects.filter(is_deleted=True).order_by('comp_code')
    if not companies.exists():
        return Response({'error' : 'No Deleted company found'})
    serializer = CompanySerializer(companies, many=True)
    return Response({'message' : 'Deleted Companies retrieved successfully', 'data' : serializer.data})


@csrf_exempt
@api_view(['POST'])
def restore_company(request):
    data = request.data   
    try:
        obj = Company.objects.get(comp_code = data['comp_code'])
        if not obj.is_deleted:
            return Response({'error' : 'Company is not deleted yet!!'})
          
    except Company.DoesNotExist:
        return Response({'error' : 'Company Not Found'}, status=404)
    
    obj.restore()
    obj.save()
    serializer = CompanySerializer(obj)
    
    return Response({'message' : 'Company Restored Successfully', 'data' : serializer.data}, status=200) 


# ----------------Branch--------------------------#

@csrf_exempt
@api_view(['POST'])
def register_branch(request):
    data = request.data

    if isinstance(data, list):
        serializer = BranchSerializer(data=data, many=True)
        if serializer.is_valid():
            branch_objects = [Branch(**item) for item in serializer.validated_data]
            Branch.objects.bulk_create(branch_objects)
            return Response({'message' : 'Branches added successfully', 'data' : serializer.data},status=201)
        return Response({'error' : serializer.errors})
    
    serializer = BranchSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Branch added successfully', 'data': serializer.data}, status=201)
    return Response({'error' : serializer.errors})

@csrf_exempt
@api_view(['GET'])
def list_branch(request):
    branches = Branch.objects.filter(is_deleted=False).order_by('branch_code')
    if not branches.exists():
        return Response({'error' : 'No Branch Details found'})
    paginator = CustomPagination()
    paginated_branches = paginator.paginate_queryset(branches,request)
    serializer = BranchSerializer(paginated_branches, many=True)
    return paginator.get_paginated_response({'message': 'Branches retrieved successfully', 'data': serializer.data})

@csrf_exempt
@api_view(['GET'])
def get_branch_details(request, branch_code):
    try:
        branch = Branch.objects.get(branch_code=branch_code, is_deleted=False)
    except Branch.DoesNotExist:
        return Response({'error' : 'No branch details found'}, status=404)
    serializer = BranchSerializer(branch)
    return Response({'message' : 'Branch retrived successfully', 'data' : serializer.data})

@csrf_exempt
@api_view(['PUT', 'PATCH'])
def update_branch(request):
    data = request.data
    try:
        obj = Branch.objects.get(branch_code=data['branch_code'])
        
        if obj.is_deleted:
            return Response({'error': 'Branch has already been deleted'})
        
    except Branch.DoesNotExist:
        return Response({'error': 'Branch Not Found'}, status=404)
    
    if request.method == 'PUT':
        serializer = BranchSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Branch details updated successfully', 'data': serializer.data})
        return Response({'error': serializer.errors}, status=400)

    elif request.method == 'PATCH':
        serializer = BranchSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Branch details updated successfully', 'data': serializer.data})
        return Response({'error': serializer.errors}, status=400)

@csrf_exempt
@api_view(['DELETE'])
def delete_branch(request,branch_code):
    try:
        obj = Branch.objects.get(branch_code=branch_code)
        if obj.is_deleted:
            return Response({'error': 'Branch has already been deleted'})
    except Branch.DoesNotExist:
        return Response({'error': 'Branch Not Found'}, status=404)
    
    obj.soft_delete()
    obj.save()

    return Response({'message': 'Branch deleted successfully'}, status=200)

@csrf_exempt
@api_view(['GET'])
def list_deleted_branch(request):
    branches = Branch.objects.filter(is_deleted=True).order_by('branch_code')
    if not branches.exists():
        return Response({'error' : 'No Deleted Branch found'})
    serializer = BranchSerializer(branches, many=True)
    return Response({'message': 'Deleted branches retrieved successfully', 'data': serializer.data})

@csrf_exempt
@api_view(['POST'])
def restore_branch(request):
    data = request.data
    try:
        obj = Branch.objects.get(branch_code=data['branch_code'])
        if not obj.is_deleted:
            return Response({'error': 'Branch is not deleted yet!'})
          
    except Branch.DoesNotExist:
        return Response({'error': 'Branch Not Found'}, status=404)
    
    obj.restore()
    obj.save()
    serializer = BranchSerializer(obj)
    
    return Response({'message': 'Branch restored successfully', 'data': serializer.data}, status=200)



# ----------------Employee------------------------#

@csrf_exempt
@api_view(['POST'])
def register_employee(request):
    data = request.data
    if isinstance(data, list):
        serializer = EmployeeSerializer(data=data, many=True)
    else:
        serializer = EmployeeSerializer(data=data)    
    if serializer.is_valid():
        if isinstance(data, list):
            Employee.objects.bulk_create([Employee(**item) for item in serializer.validated_data])
            return Response({'message': 'Employees added successfully'}, status=201)
        serializer.save()
        return Response({'message': 'Employee added successfully', 'data': serializer.data}, status=201)
    
    return Response({'error': serializer.errors}, status=400)

@csrf_exempt
@api_view(['GET'])
def list_employee(request):
    employees = Employee.objects.filter(is_deleted=False).order_by('emp_id')
    if not employees.exists():
        return Response({'error' : 'No Employee details found'})
    paginator = CustomPagination()
    paginated_employees = paginator.paginate_queryset(employees,request)
    serializer = EmployeeSerializer(paginated_employees, many=True)
    return paginator.get_paginated_response({'message': 'Employees retrieved successfully', 'data': serializer.data})

@csrf_exempt
@api_view(['GET'])
def get_employee_details(request,emp_id):
    try:
        employee = Employee.objects.get(emp_id=emp_id, is_deleted=False)
    except Employee.DoesNotExist:
        return Response({'error' : 'No Employee details found for this id'}, status=404)
    serializer = EmployeeSerializer(employee)
    return Response({'message' : 'Employee retrieved successfully', 'data' : serializer.data})

@csrf_exempt
@api_view(['PUT', 'PATCH'])
def update_employee(request):
    data = request.data
    try:
        obj = Employee.objects.get(emp_id=data['emp_id'])
        
        if obj.is_deleted:
            return Response({'error': 'Employee has already been deleted'})
        
    except Employee.DoesNotExist:
        return Response({'error': 'Employee Not Found'}, status=404)
    
    if request.method == 'PUT':
        serializer = EmployeeSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee details updated successfully', 'data': serializer.data})
        return Response({'error': serializer.errors}, status=400)

    elif request.method == 'PATCH':
        serializer = EmployeeSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee details updated successfully', 'data': serializer.data})
        return Response({'error': serializer.errors}, status=400)

@csrf_exempt
@api_view(['DELETE'])
def delete_employee(request,emp_id):
    try:
        obj = Employee.objects.get(emp_id=emp_id)
        if obj.is_deleted:
            return Response({'error': 'Employee has already been deleted'})
    except Employee.DoesNotExist:
        return Response({'error': 'Employee Not Found'}, status=404)
    
    obj.soft_delete()
    obj.save()

    return Response({'message': 'Employee deleted successfully'}, status=200)

@csrf_exempt
@api_view(['GET'])
def list_deleted_employee(request):
    employees = Employee.objects.filter(is_deleted=True).order_by('emp_id')
    if not employees.exists():
        return Response({'error' : 'No Deleted Employees found'})
    serializer = EmployeeSerializer(employees, many=True)
    return Response({'message': 'Deleted employees retrieved successfully', 'data': serializer.data})

@csrf_exempt
@api_view(['POST'])
def restore_employee(request):
    data = request.data
    try:
        obj = Employee.objects.get(emp_id=data['emp_id'])
        if not obj.is_deleted:
            return Response({'error': 'Employee is not deleted yet!'})
          
    except Employee.DoesNotExist:
        return Response({'error': 'Employee Not Found'}, status=404)
    
    obj.restore()
    obj.save()
    serializer = EmployeeSerializer(obj)
    
    return Response({'message': 'Employee restored successfully', 'data': serializer.data}, status=200)


# ----------------Filtering------------------------#

@csrf_exempt
@api_view(['GET'])
def get_branches_for_company(request, comp_code):
    try:    
        company = Company.objects.get(comp_code=comp_code, is_deleted=False)
        branches = Branch.objects.filter(comp_code=company,is_deleted=False).order_by('branch_code')
        if not branches.exists():
            return Response({'error' : 'No branches for the given company'},status=404)     
        paginator = CustomPagination()
        paginated_branches = paginator.paginate_queryset(branches, request) 
        serializer = BranchSerializer(paginated_branches, many=True)
        return paginator.get_paginated_response({'message' : 'Branches are retrieved successfully', 'data' : serializer.data})
    except Company.DoesNotExist:
        return Response({'error' : 'Company Not Found'}, status=404)
    

@csrf_exempt
@api_view(['GET'])
def get_company_for_branches(request, branch_code):
    try:
        branch = Branch.objects.get(branch_code=branch_code, is_deleted=False)
        companies = Company.objects.filter(branch=branch, is_deleted=False)
        if not companies.exists():
            return Response({'error' : 'No companies found for the given branch'},status=404)
        paginator = CustomPagination()
        paginated_companies = paginator.paginate_queryset(companies,request)
        serializer = CompanySerializer(paginated_companies, many=True)
        return paginator.get_paginated_response({'message' : 'Company retrieved successfully', 'data' : serializer.data})
    except Branch.DoesNotExist:
        return Response({'error' : 'Branch Not Found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def get_employee_for_company(request, comp_code):
    try:
        company = Company.objects.get(comp_code=comp_code, is_deleted=False)
        employees = Employee.objects.filter(comp_code=company, is_deleted=False).order_by('comp_code')
        if not employees.exists():
            return Response({'error' : 'No employees found for the given company'},status=404) 
        paginator = CustomPagination()
        paginated_empoyees = paginator.paginate_queryset(employees,request)
        serializer = EmployeeSerializer(paginated_empoyees, many=True)
        return paginator.get_paginated_response({'message' : 'Employees retrieved successfully', 'data' : serializer.data})
    except Company.DoesNotExist:
        return Response({'error' : 'Company Not Found'}, status=404)
    

@csrf_exempt
@api_view(['GET'])
def get_employee_for_branch(request, branch_code):
    try:
        branch = Branch.objects.get(branch_code=branch_code, is_deleted=False)
        employees = Employee.objects.filter(branch_code=branch,is_deleted=False).order_by('branch_code')
        if not employees.exists():
            return Response({'error' : 'No employees found for the given branch'},status=404) 
        paginator = CustomPagination()
        paginated_employees = paginator.paginate_queryset(employees,request)
        serializer = EmployeeSerializer(paginated_employees, many=True)
        return paginator.get_paginated_response({'message' : 'Employees retrieved successfully', 'data' : serializer.data})
    except Branch.DoesNotExist:
        return Response({'error' : 'Branch Does Not Exist'}, status=404)
    

@csrf_exempt
@api_view(['GET'])
def get_employees_by_company_and_branch(request, comp_code, branch_code):
    try:
        company = Company.objects.get(comp_code=comp_code, is_deleted=False)
        branch = Branch.objects.get(branch_code = branch_code, is_deleted=False)
        employees = Employee.objects.filter(comp_code = company, branch_code = branch, is_deleted = False)
        if not employees.exists():
            return Response({'error' : 'No employees found for the given company and branch'},status=404)
        paginator = CustomPagination()
        paginated_employees = paginator.paginate_queryset(employees,request)
        serializer = EmployeeSerializer(paginated_employees, many=True)
        return paginator.get_paginated_response({'message' : 'Employees retrieved successfully', 'data' : serializer.data})
    
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=404)  
    except Branch.DoesNotExist:
        return Response({'error': 'Branch not found'}, status=404)
    except Exception as e:
        return Response({'error' : str(e)}, status=400)


@csrf_exempt
@api_view(['GET'])
def get_employees_by_created_at(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    try:
        if start_date:
            start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S").astimezone(timezone.get_current_timezone())
        if end_date:
            end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").astimezone(timezone.get_current_timezone())
    except ValueError:
        return Response({'error' : 'Invalid Date Format. Use YYYY-MM-DD HH:MM:SS'})

    employees = Employee.objects.filter(is_deleted=False) 

    if start_date and end_date:
        employees = employees.filter(created_at__range=(start_date,end_date))
    elif start_date:
        employees = employees.filter(created_at__gte=start_date)
    elif end_date:
        employees = employees.filter(created_at__lte=end_date)

    if not employees.exists():
        return Response({'message' : 'No employees found for the given date range'})
    
    paginator = CustomPagination()
    paginated_employees = paginator.paginate_queryset(employees, request)
    serializer = EmployeeSerializer(paginated_employees, many=True)

    return paginator.get_paginated_response({'message' : 'Employees retrieved successfully', 'data' : serializer.data})



# ----------------Searching------------------------#

@csrf_exempt
@api_view(['GET'])
def search_employees(request):

    emp_id = request.query_params.get('emp_id')
    dept = request.query_params.get('department')
    designation = request.query_params.get('designation')
    email = request.query_params.get('email')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    comp_code = request.query_params.get('comp_code')
    branch_code = request.query_params.get('branch_code')

    employees = Employee.objects.filter(is_deleted=False)
    
    if emp_id:
        employees = employees.filter(emp_id=emp_id)
    if dept:
        employees = employees.filter(emp_dept=dept)
    if designation:
        employees = employees.filter(emp_designation=designation)
    if email:
        employees = employees.filter(emp_email=email)
    if start_date and end_date:
        try:
            start_date_obj = timezone.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = timezone.datetime.strptime(end_date, "%Y-%m-%d")
            employees = employees.filter(emp_doj__range=(start_date_obj,end_date_obj))
        except ValueError:
            return Response({'error' : 'Invalid Date Format. Please use YYYY-MM-DD'})
    if comp_code:
        employees = employees.filter(comp_code=comp_code)
    if branch_code:
        employees = employees.filter(branch_code=branch_code)    

    if not employees.exists():
        return Response({'message' : 'No Employees found matching the criteria'},status=404)
    
    paginator=CustomPagination()
    paginated_employees = paginator.paginate_queryset(employees, request)
    serializer = EmployeeSerializer(paginated_employees, many=True)
    return paginator.get_paginated_response({'message' : 'Employee retrieved successuflly', 'data' : serializer.data})