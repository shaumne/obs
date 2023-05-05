from django.db import models
from students.models.students import Students

class Taxation(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='taxation_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Taxation"
        verbose_name = "Taxation"
        verbose_name_plural = "Taxation"


    def __str__(self) -> str:
        return self.student_name
    
    