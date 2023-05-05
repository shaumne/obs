from django.db import models
from students.models.students import Students

class Introduction_To_Robotics(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='introduction_to_robotics_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Introduction To Robotics"
        verbose_name = "Introduction To Robotics"
        verbose_name_plural = "Introduction To Robotics"


    def __str__(self) -> str:
        return self.student_name
    
    