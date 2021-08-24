from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from devedor.models import Debtor, Employees

from devedor.serializers import DebtorSerializer, EmployeesSerializer

from django.core.files.storage import default_storage


##def

@csrf_exempt
def debtorAPI(request,id=0):
    if request.method=='GET':
        debtors = Debtor.objects.all()
        debtors_serializer = DebtorSerializer(debtors, many= True)
        return JsonResponse(debtors_serializer.data, safe=False)

    elif request.method=='POST':
        debtor_data=JSONParser().parse(request)
        debtor_serializer = DebtorSerializer(data=debtor_data)
        if debtor_serializer.is_valid():
             debtor_serializer.save()
             return JsonResponse("Added Successfully!!", safe= False)
        return JsonResponse("Failed to Add.", safe= False)

    elif request.method=='PUT':
        debtor_data = JSONParser().parse(request)
        debtor=Debtor.objects.get(IdDebtor=debtor_data['IdDebtor'])
        debtor_serializer=DebtorSerializer(debtor,data=debtor_data)
        if debtor_serializer.is_valid():
            debtor_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update Try Again", safe=False)
    
    elif request.method=='DELETE':
        debtor=Debtor.objects.get(IdDebtor=id)
        debtor.delete()
        return JsonResponse("Deleted Successfully", safe=False)



@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeesSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeesSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name, safe=False)