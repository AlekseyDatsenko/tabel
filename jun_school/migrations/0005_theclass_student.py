# Generated by Django 2.2.5 on 2019-11-09 22:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jun_school', '0004_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='theclass',
            name='student',
            field=models.ManyToManyField(help_text='Выберите ученика:', to=settings.AUTH_USER_MODEL),
        ),
    ]
