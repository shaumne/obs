from django.db import models
from students.models.students import Students

class Mechanical_Engineering_Design(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='mechanical_engineering_design_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Mechanical Engineering Design"
        verbose_name = "Mechanical Engineering Design"
        verbose_name_plural = "Mechanical Engineering Design"


    def __str__(self) -> str:
        return self.student_name
    
    