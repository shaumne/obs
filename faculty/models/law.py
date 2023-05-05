from django.db import models

class Law(models.Model):
    name = models.TextField(blank=False, null=False)



    class Meta:
        db_table = "Law School"
        verbose_name = "Law School"
        verbose_name_plural = "Law School"


    def __str__(self) -> str:
        return self.name
