from django.db import models
from faculty.models.faculty import Faculty


class Students(models.Model):
    student_id = models.IntegerField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    surname = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    faculty = models.ManyToManyField(Faculty, blank=False, null=False)

    class Meta:
        db_table = "Students"
        verbose_name = "Stundets"
        verbose_name_plural = "Students"


    def __str__(self) -> str:
        return self.name + " " + self.surname

