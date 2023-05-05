from django.db import models
from students.models.students import Students

class Labor_Law(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='labor_law_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Labor Law"
        verbose_name = "Labor Law"
        verbose_name_plural = "Labor Law"


    def __str__(self) -> str:
        return self.student_name
    
    