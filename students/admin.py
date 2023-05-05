from django.contrib import admin
from .models.students import Students

# Register your models here.


class MyAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'email')
        

admin.site.register(Students, MyAdmin)
