# Generated by Django 3.1.4 on 2020-12-25 11:52

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsprogram', '0021_auto_20201219_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='ApiToken',
            field=models.CharField(auto_created=True, default='ALdjwB4WJZsYG5HUjMjfyk60BRHF7wchrtPzhztLfIxtELzuNIaGSSTKFmXCqUXy', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='DateOfBart',
            field=django_jalali.db.models.jDateTimeField(verbose_name='تاریخ تولد'),
        ),
    ]
