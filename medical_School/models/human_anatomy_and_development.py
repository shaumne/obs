from django.db import models
from students.models.students import Students

class Human_Anatomy_And_Development(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='human_anatomy_and_development_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Human Anatomy And Development"
        verbose_name = "Human Anatomy And Development"
        verbose_name_plural = "Human Anatomy And Development"


    def __str__(self) -> str:
        return self.student_name
    
    