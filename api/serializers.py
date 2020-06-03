from rest_framework import  serializers
from  .models import Task

class SerializersTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

