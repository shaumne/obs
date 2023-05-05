from django.db import models
from students.models.students import Students

class Pharmacology_And_Therapeutics(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='pharmacology_and_therapeutics_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Pharmacology And Therapeutics"
        verbose_name = "Pharmacology And Therapeutics"
        verbose_name_plural = "Pharmacology And Therapeutics"


    def __str__(self) -> str:
        return self.student_name
    
    