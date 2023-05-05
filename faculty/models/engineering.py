from django.db import models

class Engineering(models.Model):
    name = models.TextField(null=False, blank=False)


    class Meta:
        db_table = "School of Engineering"
        verbose_name = "School of Engineering"
        verbose_name_plural = "School of Engineering"



    def __str__(self) -> str:
        return self.name