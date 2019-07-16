from django.urls import path
from .views import add_teacher,list_teachers,teacher_details,edit_teacher

urlpatterns=[
    path("add/",add_teacher,name="add_teacher"),
    path("list/",list_teachers,name="list_teachers"),
    path("view/<int:pk>/",teacher_details,name="teacher_details"),
    path("edit/<int:pk>/",edit_teacher,name="edit_teacher"),
]