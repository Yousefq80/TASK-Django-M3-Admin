# Generated by Django 4.0.4 on 2022-10-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name_ar',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_fr',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_jp',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
