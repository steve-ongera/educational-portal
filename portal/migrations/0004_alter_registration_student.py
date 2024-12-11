# Generated by Django 5.1.2 on 2024-12-11 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_unit_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_student': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
