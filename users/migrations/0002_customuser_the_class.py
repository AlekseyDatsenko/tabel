# Generated by Django 2.2.5 on 2019-11-09 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jun_school', '0004_delete_student'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='the_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jun_school.TheClass'),
        ),
    ]
