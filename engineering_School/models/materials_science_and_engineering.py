from django.db import models
from students.models.students import Students

class Materials_Science_And_Engineering(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='materials_science_and_engineering_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Materials Science And Engineering"
        verbose_name = "Materials Science And Engineering"
        verbose_name_plural = "Materials Science And Engineering"


    def __str__(self) -> str:
        return self.student_name
    
    