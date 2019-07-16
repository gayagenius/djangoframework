from django.contrib import admin


# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=("registration_number","first_name","last_name","date_of_birth","email","image")
    search_fields=("registration_number","first_name","last_name","date_of_birth","email")


admin.site.register(Student,StudentAdmin)
