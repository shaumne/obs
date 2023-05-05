from django.db import models
from students.models.students import Students

class Social_And_Ethical_Issues_In_Medicine(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='social_and_ethical_issues_in_medicine_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Social And Ethical Issues In Medicine"
        verbose_name = "Social And Ethical Issues In Medicine"
        verbose_name_plural = "Social And Ethical Issues In Medicine"


    def __str__(self) -> str:
        return self.student_name
    
    