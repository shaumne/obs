from django.db import models
from students.models.students import Students

class Introduction_To_Solid_State_Chemistry(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='introduction_to_solid_state_chemistry_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Introduction To Solid-State Chemistry"
        verbose_name = "Introduction To Solid-State Chemistry"
        verbose_name_plural = "Introduction To Solid-State Chemistry"


    def __str__(self) -> str:
        return self.student_name
    
    