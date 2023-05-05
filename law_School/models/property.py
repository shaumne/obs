from django.db import models
from students.models.students import Students

class Property(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='property_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Property"
        verbose_name = "Property"
        verbose_name_plural = "Property"


    def __str__(self) -> str:
        return self.student_name
    
    