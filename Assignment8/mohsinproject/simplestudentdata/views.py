from rest_framework import viewsets
from .models import StudentData
from .serializers import StudentDataSerializer

class StudentDataViewSet(viewsets.ModelViewSet):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataSerializer
