# Generated by Django 4.2.1 on 2023-05-05 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_education_engineering_law_medical_school'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Engineering',
        ),
        migrations.DeleteModel(
            name='Fine_Arts',
        ),
        migrations.DeleteModel(
            name='Law',
        ),
        migrations.DeleteModel(
            name='Medical_School',
        ),
        migrations.DeleteModel(
            name='Public_policy',
        ),
    ]