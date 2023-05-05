from django.db import models
from students.models.students import Students

class Criminal_Law_And_Procedure(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='criminal_law_and_procedure_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Criminal Law And Procedure"
        verbose_name = "Criminal Law And Procedure"
        verbose_name_plural = "Criminal Law And Procedure"


    def __str__(self) -> str:
        return self.student_name
    
    