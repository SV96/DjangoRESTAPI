from rest_framework import serializers
from webapp.models import employee

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('firstname','lastname')