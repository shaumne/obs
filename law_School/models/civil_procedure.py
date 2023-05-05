from django.db import models
from students.models.students import Students

class Civil_Procedure(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='civil_procedure_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Civil Procedure"
        verbose_name = "Civil Procedure"
        verbose_name_plural = "Civil Procedure"


    def __str__(self) -> str:
        return self.student_name
    
    