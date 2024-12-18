# Generated by Django 5.1.2 on 2024-12-11 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_customuser_is_student_customuser_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='teacher',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_teacher': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
