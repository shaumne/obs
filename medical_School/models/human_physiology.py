from django.db import models
from students.models.students import Students

class Human_Physiology(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='human_physiology_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Human Physiology"
        verbose_name = "Human Physiology"
        verbose_name_plural = "Human Physiology"


    def __str__(self) -> str:
        return self.student_name
    
    