from django.db import models
from students.models.students import Students

class International_Law(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='international_law_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "International Law"
        verbose_name = "International Law"
        verbose_name_plural = "International Law"


    def __str__(self) -> str:
        return self.student_name
    
    