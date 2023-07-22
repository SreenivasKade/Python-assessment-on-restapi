
from django import forms
from RestApp.models import Employee
 
 
# creating a form
class EmployeeForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Employee
 
        # specify fields to be used
        fields = [
            'employee_name'
        ]