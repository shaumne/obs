from django.db import models
from students.models.students import Students

class Pathways_Mechanisms_And_Models_Of_Human_Disease(models.Model):
    student_name = models.ManyToManyField(Students, blank=False, related_name='pathways_mechanisms_and_models_of_human_disease_students_name')
    exam1 = models.CharField(max_length=5)
    exam2 = models.CharField(max_length=5)
    exam3 = models.CharField(max_length=5)


    class Meta:
        db_table= "Pathways, Mechanisms, And Models Of Human Disease"
        verbose_name = "Pathways, Mechanisms, And Models Of Human Disease"
        verbose_name_plural = "Pathways, Mechanisms, And Models Of Human Disease"


    def __str__(self) -> str:
        return self.student_name
    
    