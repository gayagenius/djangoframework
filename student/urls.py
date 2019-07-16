from django.urls import path
from .views import add_student,list_students,student_details,edit_student

urlpatterns=[
    path("add/",add_student,name="add_student"),
    path("list/",list_students,name="list_students"),
    path("view/<int:pk>/",student_details,name="student_details"),
    path("edit/<int:pk>/",edit_student,name="edit_student"),
]