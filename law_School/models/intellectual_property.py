from django.db import models
from students.models.students import Students

class Intellectual_Property(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='intellectual_property_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Intellectual Property"
        verbose_name = "Intellectual Property"
        verbose_name_plural = "Intellectual Property"


    def __str__(self) -> str:
        return self.student_name
    
    