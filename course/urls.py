from django.urls import path
from .views import add_course,list_courses,course_details,edit_course

urlpatterns=[
    path("add/",add_course,name="add_course"),
    path("list/",list_courses,name="list_courses"),
    path("details/<int:pk>/",course_details,name="course_details"),
    path("edit/<int:pk>/",edit_course,name="edit_course"),
]