from django.shortcuts import render,redirect,get_object_or_404
from RestApp.models import Employee
from RestApp.forms import EmployeeForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestApp.serializers import *
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

##############################################################################
#CRUD OPERATIONS USING DJANGO
#############################################################################


#To create an employee by using form ...............................
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    form = EmployeeForm()
    if request.method == 'POST':
        # add the dictionary during initialization
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('RestApp:list')
         
    return render(request, "RestApp/create_view.html", {'form':form})



#to fetch all employee list...........................................
def list_view(request):
    e = Employee.objects.all()
    print(e)
    return render(request,'RestApp/list.html',{'e' : e})


#update existing employee by id ..................................
def update_view(request,id):
    obj = get_object_or_404(Employee, id = id)
    form = EmployeeForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('RestApp:list')
    return render(request,'RestApp/update.html',{'form':form})


# delete employee by id .............................................
def delete_view(request,id):
    context = {}
    e = Employee.objects.get(id = id)
    print(e)
    if request.method =="POST":
        # delete object
        e.delete()
        return redirect("RestApp:list")
  
    return render(request, "RestApp/delete.html", context)


###############################################################
#CRUD OPERATIONS USING REST API...............................
###############################################################

#... fetching all employee data  ....................
@api_view(['GET'])
def AllEmployeeView(request):
    data = Employee.objects.all()
    serializer = EmployeeSerializer(data, many = True)
    return Response(serializer.data)

# ... fetching emplyee data by id ..............................
@api_view(['GET'])
def EmployeeIdView(request,id):
    data = Employee.objects.get(id = id)
    serializer = EmployeeSerializer(data, many = False)
    return Response(serializer.data)


#...create new employee .......................................
@api_view(['POST'])
def EmployeeAddView(request):
    serializer = EmployeeSerializer(data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



#... update exiing employee .............................................
@api_view(['PUT'])
def UpdateEmployeeView(request, id):
    update_employee = Employee.objects.get(id = id)
    serializer = EmployeeSerializer(instance = update_employee, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



# ... delete employee by id ...................................................
@api_view(['DELETE'])
def DeleteEmployeeView(request, id):
    delete_employeeid = Employee.objects.get(id = id)
    if request.method == 'DELETE': 
        delete_employeeid.delete() 
        return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
# ... delete all employees ........................................................
@api_view(['DELETE'])
def DeleteAllEmployeeView(request):
    if request.method == 'DELETE':
        emp = Employee.objects.all()
        emp.delete()
        return JsonResponse({'message': 'all employees were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
#... fetching name contains "sa" ....................................................
@api_view(['GET'])
def GetEmployeeView(request):
    data = Employee.objects.filter(employee_name__contains='sa')
    serializer = EmployeeSerializer(data, many = True)
    return Response(serializer.data)



#... fetching employee by name ....................................................
@api_view(['GET'])
def EmployeenameView(request,employee_name):
    data = Employee.objects.filter(employee_name = employee_name)
    serializer = EmployeeSerializer(data, many = True)
    return Response(serializer.data)



