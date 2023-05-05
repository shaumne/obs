from django.db import models
from students.models.students import Students

class Introduction_To_Computer_Science_And_Programming(models.Model):
    student_name = models.ManyToManyField(Students, blank=False,related_name='introduction_to_computer_science_and_programming_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Introduction To Computer Science And Programming"
        verbose_name = "Introduction To Computer Science And Programming"
        verbose_name_plural = "Introduction To Computer Science And Programming"


    def __str__(self) -> str:
        return self.student_name
    
    