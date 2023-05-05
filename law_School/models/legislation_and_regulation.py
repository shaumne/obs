from django.db import models
from students.models.students import Students

class Legislation_And_Regulation(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='legislation_and_regulation_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Legislation And Regulation"
        verbose_name = "Legislation And Regulation"
        verbose_name_plural = "Legislation And Regulation"


    def __str__(self) -> str:
        return self.student_name
    
    