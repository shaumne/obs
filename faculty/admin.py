from django.contrib import admin
from .models.faculty import Faculty
from .models.engineering import Engineering
from .models.law import Law
from .models.medical_school import Medical_School

# Register your models here.
admin.site.register([
    Faculty,
    Medical_School,
    Engineering,
    Law
])