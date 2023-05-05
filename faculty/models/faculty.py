from django.db import models

class Faculty(models.Model):
    name = models.TextField()


    class Meta:
        db_table = "Faculty"
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty"

    def __str__(self) -> str:
        return self.name
