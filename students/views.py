from rest_framework.viewsets import ModelViewSet
from .models import Student
from rest_framework.filters import SearchFilter
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend




class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['name', 'group']
    search_fields = ['name',]






