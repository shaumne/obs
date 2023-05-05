from django.db import models
from students.models.students import Students

class Genetics_And_Genomics(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='genetics_and_genomics_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)

    class Meta:
        db_table= "Genetics And Genomics"
        verbose_name = "Genetics And Genomics"
        verbose_name_plural = "Genetics And Genomics"

    def __str__(self) -> str:
        return self.student_name
