from django.db import models
from students.models.students import Students

class Legal_Profession(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='legal_profession_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Legal Profession"
        verbose_name = "Legal Profession"
        verbose_name_plural = "Legal Profession"


    def __str__(self) -> str:
        return self.student_name
    
    