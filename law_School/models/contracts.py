from django.db import models
from students.models.students import Students

class Contracts(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='contracts_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Contracts"
        verbose_name = "Contracts"
        verbose_name_plural = "Contracts"


    def __str__(self) -> str:
        return self.student_name
    
    