from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeesSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Department created successfully ...', safe=False)
        return JsonResponse("Failed to create department ...", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        departments = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(departments, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Department updated successfully ...", safe=False)
        return JsonResponse("Failed to update department ...", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Department deleted successfully ...", safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST' :
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeesSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee added successfully ...", safe=False)
        return JsonResponse("Failed to add employee ...", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeesSerializer(employee, employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee updated successfully ...", safe=False)
        return JsonResponse("Failed to update employee ...")

    elif request.method == "DELETE":
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Employee deleted successfully ...", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


        
