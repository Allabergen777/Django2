# Generated by Django 4.2.1 on 2023-05-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default=1, max_length=12, unique=True, verbose_name='Number phone'),
            preserve_default=False,
        ),
    ]
