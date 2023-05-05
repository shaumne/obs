from django.db import models
from students.models.students import Students

class Digital_Electronics(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='digital_electronics_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Digital Electronics"
        verbose_name = "Digital Electronics"
        verbose_name_plural = "Digital Electronics"


    def __str__(self) -> str:
        return self.student_name
    
    