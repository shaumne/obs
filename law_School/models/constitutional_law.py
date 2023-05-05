from django.db import models
from students.models.students import Students

class Constitutional_Law(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='constitutional_law_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Constitutional Law"
        verbose_name = "Constitutional Law"
        verbose_name_plural = "Constitutional Law"


    def __str__(self) -> str:
        return self.student_name
    
    