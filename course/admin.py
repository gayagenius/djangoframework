from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display=("name","course_description","teacher")
    search_fields=("name","course_description","teacher__first_name","teacher__last_name","teacher__email")









admin.site.register(Course,CourseAdmin)



# Register your models here.
