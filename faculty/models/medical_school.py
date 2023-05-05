from django.db import models

class Medical_School(models.Model):
    name = models.TextField(blank=False, null=False)



    class Meta:
        db_table= "Medical School"
        verbose_name = "Medical School"
        verbose_name_plural = "Medical School"


    def __str__(self) -> str:
        return self.name
    