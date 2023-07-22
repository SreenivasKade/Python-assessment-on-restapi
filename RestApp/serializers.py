from RestApp.models import Employee
from rest_framework import serializers


# .. employee serializer .........................................
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'