from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","gender","email","profession","subject_training","id_number","image")
    search_fields=("first_name","last_name","gender","email","profession","subject_training","id_number")










admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
