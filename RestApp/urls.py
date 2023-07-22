from django.urls import path
from RestApp import views
app_name = 'RestApp'
urlpatterns = [
    #Django CRUD operations urls............................

    path('create/',views.create_view,name = 'create'),
    path('list/',views.list_view,name = 'list'),
    path('update/<str:id>/',views.update_view,name = 'update'),
    path('delete/<str:id>/',views.delete_view,name = 'delete'),
    
    # REST API CRUD operations urls.............................................
    path('api/employees',views.AllEmployeeView),
    path('api/employeeid/<str:id>',views.EmployeeIdView),
    path('api/addemployee',views.EmployeeAddView),
    path('api/updateemployee/<str:id>',views.UpdateEmployeeView),
    path('api/deleteemployee/<str:id>',views.DeleteEmployeeView),
    path('api/deleteallemployee',views.DeleteAllEmployeeView),
    path('api/employeenamewithsa',views.GetEmployeeView),
    path('api/employeename/<str:employee_name>',views.EmployeenameView),

    
]