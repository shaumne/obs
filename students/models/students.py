from django.db import models
from faculty.models.faculty import Faculty

class Students(models.Model):
    student_id = models.IntegerField(blank=False, null=False)
    full_name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    faculty = models.ManyToManyField(Faculty, blank=False)

    class Meta:
        db_table = "Students"
        verbose_name = "Students"
        verbose_name_plural = "Students"



    def __str__(self) -> str:
        return self.full_name

