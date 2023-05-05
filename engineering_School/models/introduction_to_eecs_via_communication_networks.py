from django.db import models
from students.models.students import Students

class Introduction_To_Eecs_Via_Communication_Networks(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='introduction_to_eecs_via_communication_networks_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Introduction To Eecs Via Communication Networks"
        verbose_name = "Introduction To Eecs Via Communication Networks"
        verbose_name_plural = "Introduction To Eecs Via Communication Networks"


    def __str__(self) -> str:
        return self.student_name
    
    