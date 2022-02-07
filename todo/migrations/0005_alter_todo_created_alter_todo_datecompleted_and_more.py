# Generated by Django 4.0 on 2022-01-19 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Сделать до'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False, verbose_name='Важно'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
