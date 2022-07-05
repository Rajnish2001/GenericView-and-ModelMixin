from statistics import mode
from wsgiref.validate import validator
from .models import Student
from rest_framework import serializers


def starts_with_r(value):
    if value[0] != 'R':
        raise serializers.ValidationError('Name should start with R')

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = ['id','name','roll','email','mobile','city']


    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')

    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() != 'surat':
    #         raise serializers.ValidationError('Name is Rohit and City must be Surat')
    #     return data