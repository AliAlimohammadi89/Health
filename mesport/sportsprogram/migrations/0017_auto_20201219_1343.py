# Generated by Django 3.1.4 on 2020-12-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsprogram', '0016_exercise_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='Token',
        ),
        migrations.AddField(
            model_name='personinfo',
            name='Token',
            field=models.CharField(auto_created=True, default='PP1Tw8ylQodhs5zWf5on8gXKjVZcpJ8a', max_length=32),
        ),
    ]
