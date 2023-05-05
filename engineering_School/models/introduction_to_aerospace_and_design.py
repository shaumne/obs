from django.db import models
from students.models.students import Students

class Introduction_To_Aerospace_And_Design(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='introduction_to_aerospace_and_design_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Introduction To Aerospace And Design"
        verbose_name = "Introduction To Aerospace And Design"
        verbose_name_plural = "Introduction To Aerospace And Design"


    def __str__(self) -> str:
        return self.student_name
    
    