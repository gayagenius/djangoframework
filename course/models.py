from django.db import models
from teacher.models import Teacher

class Course(models.Model):
    name=models.CharField(max_length =50)
    duration_in_months=models.SmallIntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    course_description=models.TextField()
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE, blank=True)

# Create your models here.
 

    def __str__(self):
        return self.name