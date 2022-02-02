# Generated by Django 3.1.4 on 2020-12-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsprogram', '0019_auto_20201219_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='Password',
            field=models.CharField(default='123', max_length=50, verbose_name='رمز ورود'),
        ),
        migrations.AddField(
            model_name='personinfo',
            name='Username',
            field=models.CharField(default='123', max_length=50, unique=True, verbose_name='نام کاربری'),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='ApiToken',
            field=models.CharField(auto_created=True, default='l6UIYrDZtizKnJudCodLP1zpOElr1pEmJq733jIMM8yrsWaJSJTcyEq8ILb4lVv8', max_length=64, unique=True),
        ),
    ]