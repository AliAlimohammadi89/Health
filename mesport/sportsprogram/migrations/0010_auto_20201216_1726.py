# Generated by Django 3.1.4 on 2020-12-16 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsprogram', '0009_auto_20201216_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='ExerciseGroups',
        ),
        migrations.AddField(
            model_name='exercise',
            name='ExerciseGroups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsprogram.exercisegroup'),
        ),
    ]