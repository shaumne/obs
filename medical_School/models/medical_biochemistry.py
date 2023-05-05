from django.db import models
from students.models.students import Students

class Medical_Biochemistry(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='medical_biochemistry_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Medical Biochemistry"
        verbose_name = "Medical Biochemistry"
        verbose_name_plural = "Medical Biochemistry"


    def __str__(self) -> str:
        return self.student_name
    
    