from django.db import models
from students.models.students import Students

class Immunology(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='immunology_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Immunology"
        verbose_name = "Immunology"
        verbose_name_plural = "Immunology"


    def __str__(self) -> str:
        return self.student_name
    
    