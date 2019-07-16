from django.shortcuts import render
from rest_framework import viewsets
from.serializers import StudentSerializer
from student.models import Student
from teacher.models import Teacher
from.serializers import TeacherSerializer
from course.models import Course
from.serializers import CourseSerializer




class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


# Create your views here.
